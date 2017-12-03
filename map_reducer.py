import argparse
import glob
import os.path
import re


class SquishObject:

    line_regex = re.compile("(:.+	){(.*)}")

    class Attribute:

        attribute_regex = re.compile("([a-zA-Z.]+)([~]?[?]?[=])'(.+)'")

        def __init__(self, name, value, matching_type='='):
            self.name = name
            self.value = value
            self.matching_type = matching_type

        @staticmethod
        def create_attribute(attribute_string):
            match = SquishObject.Attribute.attribute_regex.match(attribute_string)
            return SquishObject.Attribute(match.group(1), match.group(3), match.group(2))

    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    @staticmethod
    def create_squish_object(object_map_line):
        match = SquishObject.line_regex.match(object_map_line)
        name = match.group(1).strip()[1:]
        attributes_string_array = match.group(2).split(' ')
        attributes = [SquishObject.Attribute.create_attribute(x) for x in attributes_string_array]
        return SquishObject(name, attributes)

    # Hack: We compare only names, not attributes!
    def __eq__(self, other):
        return self.name == other.name


class ObjectMapExtractor:

    object_map_file_lines = ''
    valid_line_regex = re.compile("(:.+	[{]){1}([a-zA-Z.]+\~?\??='[^']+' ?)+[}]")

    def __init__(self, object_map_file_lines):
        self.object_map_file_lines = object_map_file_lines

    def extract_objects(self):
        valid_lines = set(list(filter(lambda x: self.valid_line_regex.match(x), self.object_map_file_lines)))
        self.print_invalid_lines(valid_lines)
        squish_objects = [SquishObject.create_squish_object(line) for line in valid_lines]
        return squish_objects

    def print_invalid_lines(self, valid_lines):
        not_valid_lines = set(self.object_map_file_lines) - valid_lines
        for not_valid_line in not_valid_lines:
            print "Line \"{}\" is not valid - SKIPPING".format(not_valid_line)


class ValidFilesArranger:

    file_type = ''

    def __init__(self, file_type):
        self.file_type = file_type

    def prepare_valid_files(self, files_paths_list):
        valid_files = []
        for file_path in files_paths_list:
            if os.path.exists(file_path):
                if os.path.isfile(file_path) and file_path.endswith('.' + self.file_type):
                    valid_files.append(file_path)
                else:
                    files_in_dir = glob.glob(os.path.join(file_path, "*"))
                    valid_files_in_dir = self.prepare_valid_files(files_in_dir)
                    valid_files.extend(valid_files_in_dir)
            else:
                print "File \"{}\" does not exist - SKIPPING".format(file_path)
        return valid_files


class TestScriptsExtractor:

    name_regex = re.compile("(['\"]:(.+)['\"])")

    found_squish_objects = []
    files_path_list = []

    def __init__(self, files_path_list):
        self.files_path_list = files_path_list

    def find_squish_objects(self):
        for file_path in self.files_path_list:
            with open(file_path) as file_to_read:
                lines = file_to_read.readlines()
            for line in lines:
                match = self.name_regex.search(line)
                if match:
                    self.found_squish_objects.append(SquishObject(match.group(2), ''))
        return self.found_squish_objects


def main():
    parser = argparse.ArgumentParser(description="Reduces the Squish object map by removing duplicated and 'not used' "
                                                 "entries. As 'not used' entry is considered any object inside object "
                                                 "map that is not found inside any of processed files.",
                                     epilog='The reduced map file will be saved in the script working directory with'
                                            ' name \'object.map.reduced\'')
    parser.add_argument('--o', metavar='path-to-object-map', help='Path to the Squish object map file.')
    parser.add_argument('--t', metavar='file-to-process',  nargs='+', help="File which content will be processed in "
                                                                           "order to find any references to objects "
                                                                           "from Squish object map. If a folder is "
                                                                           "given, all files recursively gathered from "
                                                                           "the folder and it's sub-folders are going "
                                                                           "to be processed.")
    args = parser.parse_args()

    # TODO: Validate arguments
    # TODO: Add support for global / local scripts files (can also contain objects references)
    files_list = ValidFilesArranger('py').prepare_valid_files(args.t)
    # TODO: ObjectMapExtractor takes list of lines, not a file path!
    objects_extractor = ObjectMapExtractor(args.o).extract_objects()
    squish_objects_in_test_files = TestScriptsExtractor(files_list).find_squish_objects()
    # TODO: Create SET_3 containing objects from SET_2 which are part of SET_1 OR are referenced by objects in SET_2


if __name__ == "__main__":
    main()


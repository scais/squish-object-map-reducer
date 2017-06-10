import argparse
import re


class SquishObject:

    class Attribute:
        def __init__(self, name, value, matching_type='='):
            self.name = name
            self.value = value
            self.matching_type = matching_type

        @staticmethod
        def create_attribute(attribute_string):
            match = re.search("([a-zA-Z.]+)([~]?[?]?[=])'(.+)'", attribute_string)
            return SquishObject.Attribute(match.group(1), match.group(3), match.group(2))

    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    @staticmethod
    def create_squish_object(object_map_line):
        match = re.search("(:.+	){(.*)}", object_map_line)
        name = match.group(1).strip()[1:]
        attributes_string_array = match.group(2).split(' ')
        attributes = [SquishObject.Attribute.create_attribute(x) for x in attributes_string_array]
        return SquishObject(name, attributes)


class ObjectMapExtractor:

    object_map_file_path = ''

    def __init__(self, object_map_file_path):
        self.object_map_file_path = object_map_file_path

    def extract_objects(self):
        # TODO: Read object map file path into list of strings
        # TODO: Return dictionary SquishObject.name:SquishObject converted from the list of strings
        return None


def main():
    parser = argparse.ArgumentParser(description='Reduces the Squish object map by removing duplicates and not used'
                                                 ' entries',
                                     epilog='The reduced map file will be saved in the script working directory with'
                                            ' name \'object.map.reduced\'')
    parser.add_argument('--o', metavar='path-to-object-map', help='Path to the Squish object map file.')
    parser.add_argument('--t', metavar='path-to-test-folder', help='Path to the folder with tests. The content of this'
                                                                   ' folder (and recursively all its sub-folders) is'
                                                                   ' going to be searched for python files starting'
                                                                   ' with \'tc_\'')
    args = parser.parse_args()

    # TODO: Validate arguments
    # TODO: Find all test files from specified folder
    # TODO: Extract all used objects from test files into SET_1
    # TODO: Add support for global / local scripts files (can also contain objects references)

    objects_extractor = ObjectMapExtractor(args.o)
    object_map_objects = objects_extractor.extract_objects()

    # TODO: Create SET_3 containing objects from SET_2 which are part of SET_1 OR are referenced by objects in SET_2


if __name__ == "__main__":
    main()


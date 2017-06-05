import argparse


class SquishObject:

    class Attribute:
        def __init__(self, name, value, matching_type='='):
            self.name = name
            self.value = value
            self.matching_type = matching_type

    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    @staticmethod
    def create_squish_object(object_map_line):
        # TODO: Create SquishObject from a line of an object map
        return SquishObject(None, None)


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

    objects_extractor = ObjectMapExtractor(args.o)
    object_map_objects = objects_extractor.extract_objects()

    # TODO: Create SET_3 containing objects from SET_2 which are part of SET_1 OR are referenced by objects in SET_2


if __name__ == "__main__":
    main()


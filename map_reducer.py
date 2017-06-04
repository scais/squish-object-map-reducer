import argparse


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


if __name__ == "__main__":
    main()


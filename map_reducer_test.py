import unittest

from map_reducer import SquishObject, ObjectMapExtractor, ValidFilesArranger


# class TestSquishObject(unittest.TestCase):
#
#     def test_parse_object_with_one_attribute(self):
#
#         line = ":Foo	{bar='buz'}"
#
#         squish_object = SquishObject.create_squish_object(line)
#
#         self.assertEqual(squish_object.name, 'Foo')
#         self.assertTrue(len(squish_object.attributes), 1)
#
#         self.assertEqual(squish_object.attributes[0].name, 'bar')
#         self.assertEqual(squish_object.attributes[0].value, 'buz')
#         self.assertEqual(squish_object.attributes[0].matching_type, '=')
#
#     def test_parse_object_with_two_attributes(self):
#
#         line = ":Foo	{bar='buz' bux='brr'}"
#
#         squish_object = SquishObject.create_squish_object(line)
#
#         self.assertEqual(squish_object.name, 'Foo')
#         self.assertTrue(len(squish_object.attributes), 1)
#
#         self.assertEqual(squish_object.attributes[0].name, 'bar')
#         self.assertEqual(squish_object.attributes[0].value, 'buz')
#         self.assertEqual(squish_object.attributes[0].matching_type, '=')
#
#         self.assertEqual(squish_object.attributes[1].name, 'bux')
#         self.assertEqual(squish_object.attributes[1].value, 'brr')
#         self.assertEqual(squish_object.attributes[1].matching_type, '=')
#
#     def test_parse_object_with_special_chars_in_name(self):
#
#         line = ":Bla.123.=-`]__[#;/.,{}()	{bar='buz'}"
#
#         squish_object = SquishObject.create_squish_object(line)
#
#         self.assertEqual(squish_object.name, 'Bla.123.=-`]__[#;/.,{}()')
#         self.assertTrue(len(squish_object.attributes), 1)
#
#     def test_parse_object_with_attribute_name_containing_dots(self):
#
#         line = ":Foo	{wo.lo.lo.loo='buz'}"
#
#         squish_object = SquishObject.create_squish_object(line)
#
#         self.assertEqual(squish_object.name, 'Foo')
#         self.assertTrue(len(squish_object.attributes), 1)
#
#         self.assertEqual(squish_object.attributes[0].name, 'wo.lo.lo.loo')
#         self.assertEqual(squish_object.attributes[0].value, 'buz')
#         self.assertEqual(squish_object.attributes[0].matching_type, '=')
#
#     def test_parse_object_with_attribute_wildcard(self):
#
#         line = ":Foo	{Bar?='buz'}"
#
#         squish_object = SquishObject.create_squish_object(line)
#
#         self.assertEqual(squish_object.name, 'Foo')
#         self.assertTrue(len(squish_object.attributes), 1)
#
#         self.assertEqual(squish_object.attributes[0].name, 'Bar')
#         self.assertEqual(squish_object.attributes[0].value, 'buz')
#         self.assertEqual(squish_object.attributes[0].matching_type, '?=')
#
#     def test_parse_object_with_attribute_regex(self):
#
#         line = ":Foo	{Bar~='buz'}"
#
#         squish_object = SquishObject.create_squish_object(line)
#
#         self.assertEqual(squish_object.name, 'Foo')
#         self.assertTrue(len(squish_object.attributes), 1)
#
#         self.assertEqual(squish_object.attributes[0].name, 'Bar')
#         self.assertEqual(squish_object.attributes[0].value, 'buz')
#         self.assertEqual(squish_object.attributes[0].matching_type, '~=')
#
#     def test_parse_object_with_special_chars_in_attribute_value(self):
#
#         line = ":Foo	{Bar='.123.=-][#;/.,{}()__'}"
#
#         squish_object = SquishObject.create_squish_object(line)
#
#         self.assertEqual(squish_object.name, 'Foo')
#         self.assertTrue(len(squish_object.attributes), 1)
#
#         self.assertEqual(squish_object.attributes[0].name, 'Bar')
#         self.assertEqual(squish_object.attributes[0].value, ".123.=-][#;/.,{}()__")
#         self.assertEqual(squish_object.attributes[0].matching_type, '=')
#
#
# class TestObjectMapExtractor(unittest.TestCase):
#
#     def test_extract_squish_objects_from_file(self):
#
#         with open('objects.map.sample') as file:
#             lines = file.readlines()
#
#         squish_objects = ObjectMapExtractor(lines).extract_objects()
#         self.assertTrue(len(squish_objects) > 0)
#
#     def test_handles_incorrect_lines(self):
#
#         with open('objects.map.sample') as file:
#             lines = file.readlines()
#
#         squish_objects_orig = ObjectMapExtractor(lines).extract_objects()
#
#         lines.append("            ")
#         lines.append(":Wololooo")
#         lines.append(":Foo  FOO")
#         lines.append(":Foo  FOO")
#         lines.append(":Foo  {Bar=''}")
#         lines.append(":Foo  {Bar='Buz' Bux=''}")
#         lines.append(":Foo  {Bar='Buz' ''}")
#
#         squish_objects = ObjectMapExtractor(lines).extract_objects()
#         self.assertTrue(len(squish_objects) == len(squish_objects_orig))


class TestValidFilesArranger(unittest.TestCase):

    def test_empty_arg_list_returns_empty_list(self):
        valid_files_list = ValidFilesArranger('foo').prepare_valid_files([])
        self.assertTrue(len(valid_files_list) == 0)

    def test_existing_file_returns_list_size_one(self):
        ValidFilesArranger('foo').prepare_valid_files(["", ""])
        self.assertTrue(False)

    def test_existing_folder_with_one_file_returns_list_size_one(self):
        pass

    def test_folder_containing_folder_containing_file_returns_list_size_one(self):
        pass

    def test_file_with_not_valid_suffix_returns_empty_list(self):
        pass

    def test_folder_containing_file_with_not_valid_suffix_returns_empty_list(self):
        pass

    def test_existing_folder_without_files_returns_emtpy_list(self):
        pass

    def test_non_existent_folder_returns_empty_list(self):
        pass

    def test_non_existent_file_returns_empty_list(self):
        pass

    def test_non_existent_files_return_empty_list(self):
        pass

    def test_non_existent_folders_return_empty_list(self):
        pass

    def test_non_existent_and_files_folders_return_empty_list(self):
        pass

if __name__ == '__main__':
    unittest.main()

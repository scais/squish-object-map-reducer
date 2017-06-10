import unittest

from map_reducer import SquishObject, ObjectMapExtractor


class TestSquishObject(unittest.TestCase):
    def test_parse_object_with_one_attribute(self):

        line = ":Foo	{bar='buz'}"

        squish_object = SquishObject.create_squish_object(line)

        self.assertEqual(squish_object.name, 'Foo')
        self.assertTrue(len(squish_object.attributes), 1)

        self.assertEqual(squish_object.attributes[0].name, 'bar')
        self.assertEqual(squish_object.attributes[0].value, 'buz')
        self.assertEqual(squish_object.attributes[0].matching_type, '=')

    def test_parse_object_with_two_attributes(self):

        line = ":Foo	{bar='buz' bux='brr'}"

        squish_object = SquishObject.create_squish_object(line)

        self.assertEqual(squish_object.name, 'Foo')
        self.assertTrue(len(squish_object.attributes), 1)

        self.assertEqual(squish_object.attributes[0].name, 'bar')
        self.assertEqual(squish_object.attributes[0].value, 'buz')
        self.assertEqual(squish_object.attributes[0].matching_type, '=')

        self.assertEqual(squish_object.attributes[1].name, 'bux')
        self.assertEqual(squish_object.attributes[1].value, 'brr')
        self.assertEqual(squish_object.attributes[1].matching_type, '=')

    def test_parse_object_with_special_chars_in_name(self):

        line = ":Bla.123.=-`]__[#;/.,{}()	{bar='buz'}"

        squish_object = SquishObject.create_squish_object(line)

        self.assertEqual(squish_object.name, 'Bla.123.=-`]__[#;/.,{}()')
        self.assertTrue(len(squish_object.attributes), 1)

    def test_parse_object_with_attribute_name_containing_dots(self):

        line = ":Foo	{wo.lo.lo.loo='buz'}"

        squish_object = SquishObject.create_squish_object(line)

        self.assertEqual(squish_object.name, 'Foo')
        self.assertTrue(len(squish_object.attributes), 1)

        self.assertEqual(squish_object.attributes[0].name, 'wo.lo.lo.loo')
        self.assertEqual(squish_object.attributes[0].value, 'buz')
        self.assertEqual(squish_object.attributes[0].matching_type, '=')

    def test_parse_object_with_attribute_wildcard(self):

        line = ":Foo	{Bar?='buz'}"

        squish_object = SquishObject.create_squish_object(line)

        self.assertEqual(squish_object.name, 'Foo')
        self.assertTrue(len(squish_object.attributes), 1)

        self.assertEqual(squish_object.attributes[0].name, 'Bar')
        self.assertEqual(squish_object.attributes[0].value, 'buz')
        self.assertEqual(squish_object.attributes[0].matching_type, '?=')

    def test_parse_object_with_attribute_regex(self):

        line = ":Foo	{Bar~='buz'}"

        squish_object = SquishObject.create_squish_object(line)

        self.assertEqual(squish_object.name, 'Foo')
        self.assertTrue(len(squish_object.attributes), 1)

        self.assertEqual(squish_object.attributes[0].name, 'Bar')
        self.assertEqual(squish_object.attributes[0].value, 'buz')
        self.assertEqual(squish_object.attributes[0].matching_type, '~=')

    def test_parse_object_with_special_chars_in_attribute_value(self):

        line = ":Foo	{Bar='.123.=-][#;/.,{}()__'}"

        squish_object = SquishObject.create_squish_object(line)

        self.assertEqual(squish_object.name, 'Foo')
        self.assertTrue(len(squish_object.attributes), 1)

        self.assertEqual(squish_object.attributes[0].name, 'Bar')
        self.assertEqual(squish_object.attributes[0].value, ".123.=-][#;/.,{}()__")
        self.assertEqual(squish_object.attributes[0].matching_type, '=')


class TestObjectMapExtractor(unittest.TestCase):

    def test_extract_squish_objects_from_file(self):

        with open('objects.map.sample') as file:
            lines = file.readlines()

        squish_objects = ObjectMapExtractor(lines).extract_objects()
        self.assertTrue(len(squish_objects) > 0)


if __name__ == '__main__':
    unittest.main()

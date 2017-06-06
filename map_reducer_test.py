import unittest

from map_reducer import SquishObject


class TestSquishObject(unittest.TestCase):

    def test_parse_object_with_one_attribute(self):

        line = ":Foo	{bar='buz'}"

        squish_object = SquishObject.create_squish_object(line)

        self.assertEqual(squish_object.name, 'Foo')
        self.assertTrue(len(squish_object.attributes), 1)

        self.assertEqual(squish_object.attributes[0].name, 'bar')
        self.assertEqual(squish_object.attributes[0].value, 'buz')
        self.assertEqual(squish_object.attributes[0].matching_type, '=')

if __name__ == '__main__':
    unittest.main()

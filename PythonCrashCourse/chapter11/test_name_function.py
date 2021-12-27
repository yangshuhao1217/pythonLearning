import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin'"""
        formatted_name = get_formatted_name('Janis', 'Joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgan Amadeus Mozart' work?"""
        formatted_name = get_formatted_name(
                'wolfgan', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgan Amadeus Mozart')

if __name__ == '__main__':
	unittest.main()

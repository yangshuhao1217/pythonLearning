import unittest
from city_functions import get_city_country_pair

class NamesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country_pair(self):
        """Do pair like 'Santiago, Chile' work?"""
        city_country = get_city_country_pair('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do pair like 'Santiago, Chile -population 5000000' work?"""
        city_country = get_city_country_pair('santiago', 'chile', population=5000000)
        self.assertEqual(city_country, 'Santiago, Chile -population 5000000')

if __name__ == '__main__':
    unittest.main()

import unittest


from employee import Employee


class TestEmployee(unittest.TestCase):
    """Test employee module."""
    

    def setUp(self):
        """Creat a Employee isntance for testing."""
        self.eric = Employee('eric', 'matthes', 65_000)


    def test_give_default_raise(self):
        """Test if defaut amount of salary works."""
        self.eric.give_raise()
        self.assertEqual(self.eric.salary, 70000)

    
    def test_give_custom_raise(self):
        """Test if annury salary amount works."""
        self.eric.give_raise(10000)
        self.assertEqual(self.eric.salary, 75000)


if __name__ == "__main__":
    unittest.main()

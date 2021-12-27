class Employee():
    """A class represent employee."""


    def __init__(self, f_name, l_name, salary):
        """Init employee."""
        self.first = f_name.title()
        self.last = l_name.title()
        self.salary = salary


    def give_raise(self, amount=5000):
        """Give a salary raise."""
        self.salary += amount

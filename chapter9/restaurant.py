class Restaurant:
    """A simple attempt to model a restaurant."""


    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """Describing restaurant."""
        print(f"This restaurant's name is {self.restaurant_name}.")
        print(f"The cuisine's type is {self.cuisine_type}.")



    def open_restaurant(self):
        """Simulating opening restaurant."""
        print(f"{self.restaurant_name} is open.")
    

    def read_number_served(self):
        """How many clients restaurant has served."""
        print(f"This restaurant has served {self.number_served}.")


    def set_number_served(self, number):
        """Set the number of customers that have been served."""
        self.number_served = number

    def increment_number_served(self, numbers):
        """Increment the number of customers who've been served."""
        self.number_served += numbers

class IceCreamStand(Restaurant):
    """A restaurant where sells icecream."""
    def __init__(self, restaurant_name, cuisine_type='ice_cream'):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        """Dispaly flavors of the restaurant."""
        print("\nWe have the following available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

big_one = IceCreamStand('The Big one')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.display_flavors()

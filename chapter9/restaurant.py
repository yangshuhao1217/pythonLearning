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

my_restaurant = Restaurant('dragon', 'chinese')

my_restaurant.set_number_served(29)
my_restaurant.read_number_served()

my_restaurant.increment_number_served()
my_restaurant.read_number_served()

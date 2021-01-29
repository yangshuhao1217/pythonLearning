class Restaurant:
    """A simple attempt to model a restaurant."""


    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """Describing restaurant."""
        print(f"This restaurant's name is {self.restaurant_name}.")
        print(f"The cuisine's type is {self.cuisine_type}.")



    def open_restaurant(self):
        """Simulating opening restaurant."""
        print(f"{self.restaurant_name} is open.")

restaurant = Restaurant('Dragon', 'chinese')
restaurant.describe_restaurant()
restaurant.open_restaurant()


class User:
    """User's info and greeting to users."""


    def __init__(self, first_name, last_name, location, hobbi):
        """Storing user info."""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.hobbi = hobbi


    def describle_user(self):
        """Describing user."""
        print(f"\n{self.first_name} {self.last_name} lives in {self.location}.")
        print(f"He likes {self.hobbi}.")



    def greet_user(self):
        """Greeting users."""
        print(f"Hi {self.first_name}, it's nice to meet you here.")

user = User('Eric', 'Henderson', 'Liverpool', 'football')
user.describle_user()
user.greet_user()


user_0 = User('Henry', 'Johonson', 'manchester', 'baseball')
print(f"Hi {user_0.first_name}, it's good to see you here.")
user_0.describle_user()

user_1 = User('Shulin', 'Yang', 'Shenyang', 'opera')
user_1.describle_user()

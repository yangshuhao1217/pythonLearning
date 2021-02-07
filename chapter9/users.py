class User:
    """User's info and greeting to users."""


    def __init__(self, first_name, last_name, location, hobbi):
        """Storing user info."""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.hobbi = hobbi
        self.login_attempt = 0


    def describle_user(self):
        """Describing user."""
        print(f"\n{self.first_name} {self.last_name} lives in {self.location}.")
        print(f"He likes {self.hobbi}.")



    def greet_user(self):
        """Greeting users."""
        print(f"Hi {self.first_name}, it's nice to meet you here.")


    def increment_login_attempts(self):
        """Increment the value of login_attempt by 1."""
        self.login_attempt += 1
        print(f"{self.first_name} has tried {self.login_attempt} times.")

    
    def reset_login_attempts(self):
        """Reset the value of attempts to 0."""
        self.login_attempt = 0

user = User('Eric', 'Henderson', 'Liverpool', 'football')
user.describle_user()
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

user.reset_login_attempts()
print(f"Login attempts: {str(user.login_attempt)}")

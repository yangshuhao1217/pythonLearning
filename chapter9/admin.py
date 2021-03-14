"""Represent a admin class."""

from user import User


class Admin(User):
    """A user has privileges."""


    def __init__(self, first_name, last_name, username, email, location):
        """Initialize admin."""
        super().__init__(first_name, last_name, username, email, location)


        self.privileges = Privileges()


class Privileges():
    """A class stores privileges of admin."""


    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")

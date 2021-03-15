from random import randint


class Die():
    """Represent dice."""


    def __init__(self, sides=6):
        """Initialize dice."""
        self.sides = sides


    def roll_die(self):
        """Return a number between 1 and the number of sides the die has."""
        return randint(1, self.sides)

# Create a die has 6 sides.
d6 = Die()


results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)


# Create a die has 10 sides, roll 10 times and show the results.
d10 = Die(sides=10)


results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of 10-sided die:")
print(results)


# Create a die has 20 sides, roll 10 times and show the results.
d20 = Die(sides=20)


results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)

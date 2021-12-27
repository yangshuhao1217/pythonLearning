import json


try:
	with open('favorite_number.json') as f:
		number = json.load(f)
except FileNotFoundError:
	number = input("What is you favorite number? ")
	with open('favorite_number.json', 'w') as f:
		json.dump(number, f)
	print("Thanks, I'll remember that.")
else:
	print(f"I know your favorite number! It's {number}.")
		

import json
filename = "username.json"
#
try:
	with open(filename) as file_object:
		username = json.load(file_object)
except FileNotFoundError:
	username = input("What is your name? ")
	with open(filename, "w") as file_object:
		json.dump(username, file_object)
		print("We\'ll remember you when you come back, " + username +"!")

else:
	print("Welcome back, " + username + "!")
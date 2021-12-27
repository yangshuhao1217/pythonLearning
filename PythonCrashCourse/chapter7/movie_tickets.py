prompt = "\nEnter your age, I'll tell you the cost of your movie ticket."
prompt += "\nEnter 'quit' to end the program. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is %15.")

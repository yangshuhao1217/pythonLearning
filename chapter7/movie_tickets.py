prompt = "\nEnter your age, I'll tell you the cost of your movie ticket."
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if int(message) < 3:
        print(0)
    elif int(message) < 12:
        print(10)
    else:
        print(15)

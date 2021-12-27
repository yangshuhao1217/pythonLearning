filename = 'learning_reason.txt'


print("Enter 'quit' when you are finished.")
while True:
    reason = input("Why you like programming? ")
    if reason == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{reason}\n")

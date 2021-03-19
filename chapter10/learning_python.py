with open('learning_python.txt') as file_object:
    contents = file_object.read()
print(contents)

filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

text_string = ''
for line in lines:
    text_string += line.rstrip()

print(text_string)

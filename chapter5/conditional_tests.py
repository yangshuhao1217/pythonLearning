car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

food = 'pizza'
print("\nIs food == 'pizza'? I think so.")
print(food == 'pizza')
print("\nIs food == 'hotdog'? I think no.")
print(food == 'hotdog')

team = 'milan'
print("\nIs team == 'milan'? I predict True.")
print(team == 'milan')
print("\nIs team == 'milano'? I predict False.")
print(team == 'milano')

instrument = 'guitar'
print("\nIs instrument == 'guitar'? I predict True.")
print(instrument == 'guitar')
print("\nIs pen == 'instrument'? I predict False.")
print(instrument == 'pen')

fruit = 'apple'
print("\nIs food == 'apple'? I predict True.")
print(fruit == 'apple')
print("\nIs food == 'tomato'? I predict False.")
print(fruit == 'tomato')

computer = 'asus'
print("\nIs computer == 'asus'? I predict True.")
print(computer == 'asus')
print("\nIs computer == 'gigabyte'? I predict False.")
print(computer == 'gigabyte')

best_os = 'linux'

if best_os == 'linux':
    print("Linux is the best operate systems for programming.")

if best_os != 'windows':
    print("Linux is the best operate systems for programming.")

good_os = 'Linux'

if good_os.lower() == 'linux':
    print("I like Linux.")

age = 80
print(age == 80)
print(age >= 100)
print(age <= 100)

print(age >= 30 and age <= 100)
if age >= 100 or age <= 90:
    print('OK')

best_teams = ['milan', 'real madrid', 'liverpool']
team = 'milan'
team_no = 'inter'

if team in best_teams:
    print(f"{team.title()} is the best team.")
if team_no not in best_teams:
    print(f"{team_no.title()} is not good.")

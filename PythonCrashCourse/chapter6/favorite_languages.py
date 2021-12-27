favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

people = ['richard', 'sansa', 'jen', 'phil', 'benji']
for name in people:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you for responding.")
    else:
        print(f"{name.title()}, I would like to invite you to take the favorite languages poll.")

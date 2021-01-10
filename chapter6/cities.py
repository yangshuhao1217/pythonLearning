cities = {
        'shanghai': {
            'country': 'china',
            'people': '24 millions',
            'fact': 'magical capital ',
            },
        'london': { 
            'country': 'great britain',
            'people': '8.9 millions',
            'fact': 'a lot of big football clubs',
            },
        'new york': {
            'country': 'usa',
            'people': '8.2 millions',
            'fact': 'the Status of Liberty',
            },
        }
print("Here are some information about three cities in the world!")

for name, info in cities.items():
    print(f"\nCity name: {name.title()}")
    for item, content in info.items():
        print(f"{item.title()}:")
        print(content)

print("\nSo, which city are you interested in? And were would you like to go?")

favorite_numbers = {
        'zidane': [10, 5, 8],
        'messi': [10, 19],
        'ronaldo': [7, 17],
        'ibramovich': [8, 9, 10, 11,],
        'bastern': [9, 10],
        }
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}:")
    for number in numbers:
        print(number)

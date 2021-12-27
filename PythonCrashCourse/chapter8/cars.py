def build_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything about a car."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car_profile = build_car(
        'subaru', 'outback',
        color='blue',
        tow_package=True)

print(car_profile)

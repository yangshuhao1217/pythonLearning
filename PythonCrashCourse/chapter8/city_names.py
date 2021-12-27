def city_country(city_name, country_name):
    """Return city-country pair."""
    pair = f"{city_name.title()}, {country_name.title()}"
    return pair
pair_0 = city_country('santiago', 'chile')
print(pair_0)
pair_0 = city_country('paris', 'france')
print(pair_0)
pair_0 = city_country('berlin', 'germany')
print(pair_0)

def get_city_country_pair(city, country, population=0):
    """Generate a neatly city country pair."""
    if population:
        city_country = f"{city.title()}, {country.title()} -population {population}"
    else:
        city_country = f"{city.title()}, {country.title()}"
    return city_country

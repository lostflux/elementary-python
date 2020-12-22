# Filename: city.py
# Author: Amittai Joel Wekesa
# Date: 28 October, 2020
# Purpose: City class


class City:
    def __init__(self, country_code, name, region, population, latitude, longitude):
        self.country_code = country_code
        self.name = name
        self.region = region
        self.population = population
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"{self.name},{self.population},{self.latitude},{self.longitude}"


# Filename: city.py
# Author: Amittai Joel Wekesa
# Date: 28 October, 2020
# Purpose: City driver


# Imports:
from city import City

# Initializing the list of cities:
list_of_cities = []

# Parsing the source file:
source_file = open("world_cities.txt", "r")
for line in source_file:
    stripped_line = line.strip()
    elements = stripped_line.split(",")
    country_code = elements[0]
    city_name = elements[1]
    region = elements[2]
    population = int(elements[3])
    latitude = float(elements[4])
    longitude = float(elements[5])
    list_of_cities.append(City(country_code, city_name, region, population, latitude, longitude))
source_file.close()

# Writing to the output file:
output_file = open("cities_out.txt", "w")
for city in list_of_cities:
    output_file.write(city.__str__())
    if list_of_cities[-1] != city:  # To avoid adding new line at end of file
        output_file.write("\n")
output_file.close()

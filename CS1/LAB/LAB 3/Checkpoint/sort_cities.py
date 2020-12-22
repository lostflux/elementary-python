from quicksort import sort
from cities_driver import list_of_cities


# Function to compare cities by name:
def compare_alpha(a, b):
    return a.name.lower() < b.name.lower()


# Function to compare cities by population:
def compare_population(a, b):
    return a.population >= b.population


# Function to compare cities by latitude:
def compare_latitude(a, b):
    return a.latitude < b.latitude


# Function to sort by alphabet and write results to file:
def sort_cities_alpha(list_of_cities):
    # sort alpha
    sort(list_of_cities, compare_func=compare_alpha)

    output_file = open("cities_alpha.txt", "w")

    for city in list_of_cities:
        output_file.write(f"{city}\n")

    output_file.close()
    # return list_of_cities


# Function to sort by population and write results to file:
def sort_cities_population(list_of_cities=list_of_cities):
    sort(list_of_cities, compare_func=compare_population)

    output_file = open("cities_population.txt", "w")

    for city in list_of_cities:
        output_file.write(f"{city}\n")

    output_file.close()

    return list_of_cities


# Function to sort by latitude and write results to file:
def sort_cities_latitude(list_of_cities):
    sort(list_of_cities, compare_func=compare_latitude)

    output_file = open("cities_latitude", "w")

    for city in list_of_cities:
        output_file.write(f"{city}\n")

    output_file.close()


# Function calls:
sort_cities_alpha(list_of_cities)

sort_cities_population(list_of_cities)

sort_cities_latitude(list_of_cities)


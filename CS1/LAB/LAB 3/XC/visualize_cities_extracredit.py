# Filename: visualize_cities_extracredit.py
# Author: Amittai Joel Wekesa
# Date: November 7, 2020
# Purpose: Visualizing the 50 most-populous cities

# Imports:
from cs1lib import *


# Loading image and defining constants for image width and height:
img = load_image("world_colored.png")

# Initializing CONSTANTS and variables
IMAGE_WIDTH = 720
IMAGE_HEIGHT = 360
WINDOW_TITLE = "CITIES WITH LARGEST POPULATION"
city_index = 0
frames = 0
scaled_x, scaled_y = 0, 0
city_name, current_population = "", ""
previous_cities = []
longitudes, latitudes, city_names, city_populations = [], [], [], []


# Opening the input file and reading data, saving it into two lists for convenience
input_file = open("cities_population.txt", "r")

# Parsing input file and saving data to appropriate lists
cities_count = 0
for line in input_file:
    if cities_count > 50:  # Stop at 50th most populous city
        break
    else:
        line.strip()
        longitude = float(line.split(",")[3])
        latitude = float(line.split(",")[2])
        city_name = line.split(",")[0]
        city_population = line.split(",")[1]

        longitudes.append(longitude)
        latitudes.append(latitude)
        city_names.append(city_name)
        city_populations.append(city_population)
        cities_count += 1

# Close the input file
input_file.close()


# main() function to be passed into start_graphics:
def main():

    # Calling global variables
    global city_index, frames, scaled_x, scaled_y, city_name, current_population, previous_cities
    draw_image(img, 0, 0)

    # For first 50 cities only:
    if city_index < 50:
        if frames != 0 and frames % 30 == 0:
            x = longitudes[city_index]
            y = latitudes[city_index]
            city_name = f" {city_index + 1}: {city_names[city_index]}"
            current_population = f"{city_names[city_index]}'s population: {city_populations[city_index]}"

            # Scaling the index coordinates to fit window coordinates
            scaled_x = (2 * x) + 360
            scaled_y = (90 - y) * IMAGE_HEIGHT / 180
            city_index += 1

            if len(previous_cities) < 50:
                previous_cities.append([scaled_x, scaled_y])

    # Else, reset city_index to keep the loop running!
    else:
        city_index = 0

    # Draw all the other previous cities:
    set_stroke_width(5)
    set_stroke_color(1, 20/255, 147/255, 1)
    for coordinates in previous_cities[:-1]:
        long = coordinates[0]
        lat = coordinates[1]
        draw_point(long, lat)

    # Draw current city, rank, and population
    set_stroke_width(10)
    set_stroke_color(1, 74/255, 73/255, 1)
    draw_point(scaled_x, scaled_y)
    set_font_bold()
    set_font("Times New Roman")
    set_font_size(10)
    draw_text(city_name, scaled_x + 20, scaled_y)
    set_font_size(15)
    draw_text(current_population, 0, IMAGE_HEIGHT - 20)

    # Increment the frames variable
    frames += 1


# Passing the main() function into start_graphics
start_graphics(main, title=WINDOW_TITLE, width=IMAGE_WIDTH, height=IMAGE_HEIGHT)

# Filename: visualize_cities.py
# Author: Amittai Joel Wekesa
# Date: November 7, 2020
# Purpose: Visualizing the 50 most-populous cities

from cs1lib import *


# Loading image and defining constants for image width and height:
img = load_image("world.png")
IMAGE_WIDTH = 720
IMAGE_HEIGHT = 360
WINDOW_TITLE = "CITIES WITH LARGEST POPULATION"
city_index = 0
frames = 0
scaled_x, scaled_y = 0, 0
previous_cities = []
longitudes, latitudes = [], []

# Opening the input file and reading data, saving it into two lists for convenience
input_file = open("cities_population.txt", "r")

cities_count = 0
for line in input_file:
    if cities_count > 50:  # Stop at 50th most populous city
        break
    else:
        line.strip()
        longitude = float(line.split(",")[3])
        latitude = float(line.split(",")[2])

        longitudes.append(longitude)
        latitudes.append(latitude)
        cities_count += 1

input_file.close()


# main() function to be passed into start_graphics:
def main():
    global city_index, frames, scaled_x, scaled_y, previous_cities
    draw_image(img, 0, 0)

    # if frames % 2 == 0:

    if city_index < 50:
        if frames != 0 and frames % 5 == 0:

            x = longitudes[city_index]
            y = latitudes[city_index]

            # Scaling the index coordinates to fit window coordinates
            scaled_x = (2 * x) + 360
            scaled_y = (90 - y) * IMAGE_HEIGHT / 180

            print(city_index)
            city_index += 1

            # Adding city to list of already drawn cities
            if len(previous_cities) < 50:
                previous_cities.append([scaled_x, scaled_y])

    set_stroke_width(5)
    set_stroke_color(1, 20/255, 147/255, 1)
    for coordinates in previous_cities[:-1]:
        long = coordinates[0]
        lat = coordinates[1]
        draw_point(long, lat)

    set_stroke_width(10)
    set_stroke_color(1, 0, 0, 1)
    draw_point(scaled_x, scaled_y)
    frames += 1


start_graphics(main, title=WINDOW_TITLE, width=IMAGE_WIDTH, height=IMAGE_HEIGHT)

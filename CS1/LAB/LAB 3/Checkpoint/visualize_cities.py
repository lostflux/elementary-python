from cs1lib import *


# Loading image and defining constants for image width and height:
img = load_image("world.png")
IMAGE_WIDTH = 720
IMAGE_HEIGHT = 360
city_index = 0
frames = 0
scaled_x, scaled_y = 0, 0


input_file = open("cities_population.txt", "r")

longitudes, latitudes = [], []

cities_count = 0
for line in input_file:
    if cities_count > 50:
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
    global city_index, frames, scaled_x, scaled_y
    draw_image(img, 0, 0)

    if frames % 2 == 0:

        x = longitudes[city_index]
        y = latitudes[city_index]

        scaled_x = (2 * x) + 360
        scaled_y = (90 - y) * IMAGE_HEIGHT / 180
    if frames % 20 == 0:
        city_index += 1
        if city_index > 50:
            city_index = 0
    frames += 1
    set_stroke_width(5)
    set_stroke_color(1, 0, 0, 1)
    draw_point(scaled_x, scaled_y)


    # for i in range(50):
    #     x = longitudes[i]
    #     y = latitudes[i]
    #
    #     scaled_x = (2 * x) + 360
    #     scaled_y = (90 - y) * IMAGE_HEIGHT / 180
    #     set_stroke_width(5)
    #     draw_point(scaled_x, scaled_y)


start_graphics(main, width=IMAGE_WIDTH, height=IMAGE_HEIGHT)

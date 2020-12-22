# File Name: load_story.py
# Author: Amittai Joel Siavava Wekesa -- Modified original file provided
# Date: November 09, 2020
# Purpose: Parse a story in a provided text file and create a properly formatted graph.

# Imports:
from vertex import Vertex


# Function to parse and partition lines in text file
def parse_line(line):
    section_split = line.split("|")
    vertex_name = section_split[0].strip()

    adjacent_vertices = section_split[1].strip().split(",")

    # add all except empty strings
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    text = section_split[2].strip()

    return vertex_name, adjacent, text


# Function to create graph for story.
def load_story(filename):

    vertex_dict = {}

    # Read the lines in the file into a list of lines:
    file = open(filename, "r")

    for l in file:

        # if this is a line in the correct format:
        if len(l.split("|")) == 3:
            vertex_name, adjacent_vertices, text = parse_line(l)

            # YOU WRITE THIS PART
            # create a graph vertex here and add it to the dictionary
            vertex_dict[vertex_name] = Vertex(vertex_name, adjacent_vertices, text)
    file.close()

    return vertex_dict

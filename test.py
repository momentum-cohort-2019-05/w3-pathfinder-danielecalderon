def read_line_of_ints(text):
    """Given a string with integers in it, return a list of those integers."""
    ints = []
    ints_as_strs = split_line(text)

    # equivalent code to the for loop below
    # index = 0
    # while index < len(ints_as_strs):
    #     int_as_str = ints_as_strs[index]
    #     ints.append(int(int_as_str))
    #     index += 1

    for int_as_str in ints_as_strs:
        ints.append(int(int_as_str))
    return ints


def split_line(line):
    return line.split()


def read_file_into_list(filename):
    """Given a file, return a list of each line in the file as a string."""
    with open(filename) as file:
        return file.readlines()


def read_file_into_ints(filename):
    """Given a filename, read that file and then convert it to a list
    of lists of ints. Example:
    We have a file with these contents:
    1 2
    3 4
    The return value would be [[1, 2], [3, 4]]
    """
    lines = read_file_into_list(filename)

    list_of_lists = []
    for line in lines:
        list_of_lists.append(read_line_of_ints(line))
    return list_of_lists


class ElevationMap:
    """
    ElevationMap is a class that takes a matrix (list of lists, 2D)
    of integers and can be used to generate an image of those elevations
    like a standard elevation map.
    """

    def __init__(self, elevations):
        self.elevations = elevations

    def elevation_at_coordinate(self, x, y):
        return self.elevations[y][x]

    def min_elevation(self):
        return min([min(row) for row in self.elevations])

    def max_elevation(self):
        return max([max(row) for row in self.elevations])

    def intensity_at_coordinate(self, x, y):
        """Given an x, y coordinate, return the
        intensity level (used for grayscale in image) of
        the elevation at that coordinate.
        """
        elevation = self.elevation_at_coordinate(x, y)
        min_elevation = self.min_elevation()
        max_elevation = self.max_elevation()

        return (elevation - min_elevation) / (max_elevation - min_elevation)


def draw_grayscale_gradient(filename, width, height):
    image = Image.new(mode='L', size=(width, height))
    for x in range(width):
        for y in range(height):
            image.putpixel((x, y), (int(x / width * 255),))
    image.save(filename)


if __name__ == "__main__":
    my_str = "10 12 9 345 2 78"
    read_line_of_ints(my_str)

    elevations = read_file_into_ints('elevation_test.txt')

    e_map = ElevationMap(elevations)
    print(e_map.intensity_at_coordinate(1, 2))

    draw_grayscale_gradient('test.png', 400, 400)




=====================================================






from PIL import Image
import os

from numpy import *


def read_line_of_ints(text):
    """Given a string with integers in it, return a list of those integers."""
    ints = []   
    ints_as_strs = split_line(text)


    for int_as_str in ints_as_strs:
        ints.append(int(int_as_str))
    print (ints)


def read_file_into_list(filename):
    # """Given a file, return a list of each line in the file as a string."""
    with open("elevation_small.txt") as file:
        return file.readlines()
        
#read_file_into_list("elevation_small.txt")

def read_file_into_ints(filename):
    list_of_lists = []
    lines = read_file_into_list(filename)
    for line in lines:
        list_of_lists.append(read_line_of_ints(lines))
        return list_of_lists

read_file_into_ints("elevation_small.txt")

#read_file_into_list("elevation_small.txt")
#return list_of_lists



    def __init__(self, elevations):
        self.elevations = elevations

    def elevation_at_coordinate(self, x, y):
        return self.elevations[y][x]

    def min_elevation(self):
        return min([min(row) for row in self.elevations])

    def max_elevation(self):
        return max([max(row) for row in self.elevations])

    def intensity_at_coordinate(self, x, y):
        """Given an x, y coordinate, return the
        intensity level (used for grayscale in image) of
        the elevation at that coordinate.
        """
        elevation = self.elevation_at_coordinate(x, y)
        min_elevation = self.min_elevation()
        max_elevation = self.max_elevation()

        return (elevation - min_elevation) / (max_elevation - min_elevation)

    def draw_my_map(filename, width, height):
        image = Image.new('RGBA', (width, height), 'white')
        for x in range(width):
            for y in range(height):
              '''image.putpixel((x, y), (int(x / width * 255),))'''
              image.save("map.png")
              draw_test = ImageDraw.Draw(image)
              image.show()
              print("done")



# # def draw_my_map(filename, width, height):
# #     image = Image.new(mode='L', size=(width, height))
# #     for x in range(width):
# #         for y in range(height):
# #             image.putpixel((x, y), (int(x / width * 255),))
# #             image.save("map.png")





if __name__ == "__main__":
    # my_str = "list_of_lists"
    # read_line_of_ints(list_of_lists)

    elevations = read_file_into_ints("elevation_small.txt")

    my_map = ElevationMap(elevations)
    print(my_map.intensity_at_coordinate(1, 2))

    #draw_my_map('map.png', 400, 400)



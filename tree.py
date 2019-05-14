from PIL import Image, ImageDraw
import numpy as np


class TreeFractal:
    def __init__(self, width=1920, height=1080, base_length=200, background_color=(255, 255, 255, 0)):
        """
        Initializes the tree generation process
        :param width: The width of the drawing canvas
        :param height: The height of the drawing canvas
        :param base_length: The length in px that the first cube should have
        :param background_color: The background color of the drawing canvas
        """

        self.start_coords = ((width / 2 - base_length / 2, height),
                             (width / 2 + base_length / 2, height))

        self.canvas = (width, height)

        self.background_color = background_color

        self.image = Image.new('RGBA', self.canvas, self.background_color)
        self.draw = ImageDraw.Draw(self.image)

    @staticmethod
    def __convert_list_to_tuple(*args):
        """
        Converts multiple tuple/array-like objects to a list of tuples
        :param args: Multiple tuple/array-like objects
        :return: Returns a list of tuples
        """

        return [tuple(x) for x in args]

    def __draw_cube(self, p1, p2, fill=None, outline=(0, 0, 0)):
        """
        Calculates the unknown points of the cube, then draws the cube and returns the points
        :param p1: The first known point of the cube, given as a tuple
        :param p2: The second known point of the cube, given as a tuple
        :param fill: The color the infill should have
        :param outline: The color the outline should have
        :return: Returns the 2 newly calculated points that were not known before
        """

        p1_to_p2 = np.subtract(p1, p2)
        p1_to_p4 = (-p1_to_p2[1], p1_to_p2[0])

        p3 = np.add(p2, p1_to_p4)
        p4 = np.add(p1, p1_to_p4)

        self.draw.polygon(self.__convert_list_to_tuple(p1, p2, p3, p4), fill=fill, outline=outline)

        return p3, p4

    def __draw_triangle(self, p1, p2, fill=None, outline=(0, 0, 0)):
        """
        Calculates the unknown point of the triangle, then draws the cube and returns the points
        :param p1: The first known point of the triangle, given as a tuple
        :param p2: The second known point of the triangle, given as a tuple
        :param fill: The color the infill should have
        :param outline: The color the outline should have
        :return: Returns 2x2 Points, which are the edges the cubes are based on
        """

        p1_to_p2_center = np.divide(np.subtract(p1, p2), 2)
        p1_to_p2_center_to_p3 = (p1_to_p2_center[1], -p1_to_p2_center[0])

        p3 = np.add(p2, np.add(p1_to_p2_center, p1_to_p2_center_to_p3))

        self.draw.polygon(self.__convert_list_to_tuple(p1, p2, p3), fill=fill, outline=outline)

        return (p3, p1), (p2, p3)

    @staticmethod
    def __default_style_gen(depth, shape=None):
        """
        Default function for coloring the tree
        :param depth: The current depth to base the style on
        :param shape: Either "cube" or "triangle", based on the current shape
        :return: Returns the style that the current shape should have
        """

        if depth <= 2:
            fill = (100, 54, 15)
        elif depth <= 5:
            fill = (162, 96, 41)
        else:
            fill = (38, 196, 64)
        return {"fill": fill, "outline": (0, 0, 0)}

    def generate(self, style_gen=None, depth=12, background_color=None):
        """
        Draws the Tree on the canvas
        :param style_gen: Uses a this color style if given, otherwise falling back to default
        :param depth: The depth at which the tree should be generated
        :param background_color: Uses this as the background color, otherwise fallback to initial value
        :return: Nothing

        """
        background_color = background_color if background_color is not None else self.background_color
        self.draw.rectangle([(0, 0), self.canvas], fill=background_color)

        style_gen = style_gen if style_gen is not None else self.__default_style_gen

        coord_sets = [self.start_coords]
        next_coord_sets = []

        for current_depth in range(depth):
            for coord_set in coord_sets:
                cube_coord_set = self.__draw_cube(
                    *coord_set,
                    **style_gen(current_depth, shape="cube")
                )

                triangle_coord_sets = self.__draw_triangle(
                    *cube_coord_set,
                    **style_gen(current_depth, shape="triangle")
                )

                [next_coord_sets.append(triangle_coord_set) for triangle_coord_set in triangle_coord_sets]

            coord_sets = next_coord_sets
            next_coord_sets = []

    def save(self, filename):
        """
        Saves the image canvas to a file
        :param filename: The filename the image should be saved to
        :return: Nothing
        """

        self.image.save(filename)
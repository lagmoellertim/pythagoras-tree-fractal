from PIL import Image, ImageDraw
import numpy as np
import math


class TreeFractal:
    def __init__(self, width=1920, height=1080, base_length=200, background_color=(255, 255, 255, 0), offset_x=0, offset_y=0):
        """
        Initializes the tree generation process
        :param width: The width of the drawing canvas
        :param height: The height of the drawing canvas
        :param base_length: The length in px that the first cube should have
        :param background_color: The background color of the drawing canvas
        :param offset_x: Offset of Tree Fractal on the x-axis
        :param offset_y: Offset of Tree Fractal on the y-axis
        """

        self.start_coords = ((width / 2 - base_length / 2 + offset_x, height-offset_y),
                             (width / 2 + base_length / 2 + offset_x, height-offset_y))

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

    def __draw_triangle(self, p1, p2, fill=None, outline=(0, 0, 0), angle=45, mirror=False):
        """
        Calculates the unknown point of the triangle, then draws the cube and returns the points
        :param p1: The first known point of the triangle, given as a tuple
        :param p2: The second known point of the triangle, given as a tuple
        :param fill: The color the infill should have
        :param outline: The color the outline should have
        :param angle: The angle alpha which the triangle should have
        :param mirror: Whether the triangle should be mirrored (angles swapped)
        :return: Returns 2x2 Points, which are the edges the cubes are based on
        """

        angle1 = math.pi * ((90 - angle) / 180)
        angle2 = math.pi * (angle / 180)
        if mirror:
            angle1, angle2 = angle2, angle1
        angle3 = math.pi - angle1 - angle2

        p1_to_p2 = np.subtract(p2,p1)

        length_p1_to_p2 = np.linalg.norm(p1_to_p2)
        length_p1_to_p3 = length_p1_to_p2 * math.sin(angle2) / math.sin(angle3)

        x, y = p1_to_p2

        equation_1 = p1[0] * x + p1[1] * y + length_p1_to_p3 * length_p1_to_p2 * math.cos(angle1)
        equation_2 = p2[1] * x - p2[0] * y + length_p1_to_p3 * length_p1_to_p2 * math.sin(angle1)

        x3 = ((1 / length_p1_to_p2)**2) * (x * equation_1 - y * equation_2)
        y3 = ((1 / length_p1_to_p2)**2) * (y * equation_1 + x * equation_2)

        p3 = (x3,y3)

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

    def generate(self, style_gen=None, depth=12, background_color=None, angle=90, mirror=False):
        """
        Draws the Tree on the canvas
        :param style_gen: Uses a this color style if given, otherwise falling back to default
        :param depth: The depth at which the tree should be generated
        :param background_color: Uses this as the background color, otherwise fallback to initial value
        :param angle: The angle alpha which the triangles should have
        :param mirror: This will horizontally flip the tree fractal if set to True
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
                    **style_gen(current_depth, shape="triangle"),
                    angle=angle,
                    mirror=mirror
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

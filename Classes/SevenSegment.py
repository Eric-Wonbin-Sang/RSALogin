import cv2

from Classes import Digit


class SevenSegment:

    digit_list = Digit.get_digit_list()
    positive_threshold = 120

    def __init__(self, display, idx,  y_start, y_end, x_start, x_end):

        self.display = display
        self.idx = idx

        self.y_start = y_start
        self.y_end = y_end
        self.x_start = x_start
        self.x_end = x_end

        self.image = self.display.image[self.y_start:self.y_end, self.x_start:self.x_end]
        self.image_height, self.image_width = self.get_init_dimensions()

        self.point_dict = self.get_point_dict()
        self.color_dict = self.get_color_dict()
        self.truth_dict = self.get_truth_dict()
        self.value = self.get_digit()

    def show(self):
        image_copy = self.image.copy()
        for key, (x, y) in self.point_dict.items():
            image_copy = cv2.circle(image_copy, (int(x), int(y)), radius=1, color=(255, 0, 0), thickness=-1)
        cv2.imshow("SevenSegment {}".format(self.idx), image_copy)

    def get_init_dimensions(self):
        return self.image.shape[0], self.image.shape[1]

    def get_point_dict(self):
        return {
            "top_point": (self.image_width * .5, self.image_height * .21),
            "top_left_point": (self.image_width * .22, self.image_height * .3),
            "top_right_point": (self.image_width * .85, self.image_height * .4),
            "mid_point": (self.image_width * .5, self.image_height * .52),
            "bot_left_point": (self.image_width * .2, self.image_height * .7),
            "bot_right_point": (self.image_width * .8, self.image_height * .7),
            "bot_point": (self.image_width * .5, self.image_height * .86)
        }

    def get_color_dict(self):
        color_dict = {}
        for key, (x, y) in self.point_dict.items():
            color_dict[key] = self.image[int(y), int(x)]
        return color_dict

    def get_truth_dict(self):
        truth_dict = {}
        for key, color in self.color_dict.items():
            truth_dict[key] = color < self.positive_threshold
        return truth_dict

    def get_digit(self):
        for digit in self.digit_list:
            if digit.is_digit(self.truth_dict):
                return digit.value

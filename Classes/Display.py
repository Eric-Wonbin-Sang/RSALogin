import cv2

from Classes import SevenSegment


class Display:

    def __init__(self, image):

        self.image = image
        self.seven_segment_list = self.get_seven_segment_list()
        self.value_list = [s.get_digit() for s in self.seven_segment_list]

    def get_seven_segment_list(self):

        standard_width = 29
        standard_offset = 16
        fourth_digit_offset = 17

        seven_segment_list = []
        for i in range(6):

            x_start = i * standard_width + standard_offset
            x_end = (i * standard_width) + standard_width + standard_offset

            if i >= 3:
                x_start += fourth_digit_offset
                x_end += fourth_digit_offset

            seven_segment_list.append(
                SevenSegment.SevenSegment(
                    display=self,
                    idx=i,
                    y_start=0,
                    y_end=self.image.shape[0],
                    x_start=x_start,
                    x_end=x_end
                )
            )
        return seven_segment_list

    def show(self):
        cv2.imshow('Display', self.image)

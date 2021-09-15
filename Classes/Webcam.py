import cv2


class Webcam:

    def __init__(self, camera_index, cap):

        self.camera_index = camera_index
        self.cap = cap

        self.init_height, self.init_width = self.get_init_dimensions()
        self.y_start = int(self.init_height * 5/10)
        self.y_end = int(self.init_height * 6.2/10)
        self.x_start = int(self.init_width * 5/10)
        self.x_end = int(self.init_width * 8.5/10)

        self.frame = self.set_transformed_frame()

    def get_init_dimensions(self):
        ret, frame = self.cap.read()
        return frame.shape[0], frame.shape[1]

    def set_frame(self):
        ret, frame = self.cap.read()
        self.frame = frame
        return self.frame

    def set_transformed_frame(self):
        ret, self.frame = self.cap.read()
        self.frame = self.frame[self.y_start:self.y_end, self.x_start:self.x_end]
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        # self.frame = apply_brightness_contrast(self.frame, brightness=64, contrast=64)
        return self.frame


def get_webcam(camera_index):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        return None
    return Webcam(camera_index, cap)


def apply_brightness_contrast(input_img, brightness=0, contrast=0):
    # https://www.py4u.net/discuss/15482
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow) / 255
        gamma_b = shadow

        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()

    if contrast != 0:
        f = 131 * (contrast + 127) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127 * (1 - f)

        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    return buf

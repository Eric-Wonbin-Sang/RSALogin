
class Digit:

    def __init__(self, value, has_top, has_top_left, has_top_right, has_mid, has_bot_left, has_bot_right, has_bot):

        self.value = value
        self.has_top = has_top
        self.has_top_left = has_top_left
        self.has_top_right = has_top_right
        self.has_mid = has_mid
        self.has_bot_left = has_bot_left
        self.has_bot_right = has_bot_right
        self.has_bot = has_bot

    def is_digit(self, truth_dict):
        return all(
            [
                truth_dict["top_point"] == self.has_top,
                truth_dict["top_left_point"] == self.has_top_left,
                truth_dict["top_right_point"] == self.has_top_right,
                truth_dict["mid_point"] == self.has_mid,
                truth_dict["bot_left_point"] == self.has_bot_left,
                truth_dict["bot_right_point"] == self.has_bot_right,
                truth_dict["bot_point"] == self.has_bot,
            ]
        )


def get_digit_list():
    return [
        Digit(
            value=0,
            has_top=True,
            has_top_left=True,
            has_top_right=True,
            has_mid=False,
            has_bot_left=True,
            has_bot_right=True,
            has_bot=True
        ),
        Digit(
            value=1,
            has_top=False,
            has_top_left=False,
            has_top_right=True,
            has_mid=False,
            has_bot_left=False,
            has_bot_right=True,
            has_bot=False
        ),
        Digit(
            value=2,
            has_top=True,
            has_top_left=False,
            has_top_right=True,
            has_mid=True,
            has_bot_left=True,
            has_bot_right=False,
            has_bot=True
        ),
        Digit(
            value=3,
            has_top=True,
            has_top_left=False,
            has_top_right=True,
            has_mid=True,
            has_bot_left=False,
            has_bot_right=True,
            has_bot=True
        ),
        Digit(
            value=4,
            has_top=False,
            has_top_left=True,
            has_top_right=True,
            has_mid=True,
            has_bot_left=False,
            has_bot_right=True,
            has_bot=False
        ),
        Digit(
            value=5,
            has_top=True,
            has_top_left=True,
            has_top_right=False,
            has_mid=True,
            has_bot_left=False,
            has_bot_right=True,
            has_bot=True
        ),
        Digit(
            value=6,
            has_top=True,
            has_top_left=True,
            has_top_right=False,
            has_mid=True,
            has_bot_left=True,
            has_bot_right=True,
            has_bot=True
        ),
        Digit(
            value=7,
            has_top=True,
            has_top_left=True,
            has_top_right=True,
            has_mid=False,
            has_bot_left=False,
            has_bot_right=True,
            has_bot=False
        ),
        Digit(
            value=8,
            has_top=True,
            has_top_left=True,
            has_top_right=True,
            has_mid=True,
            has_bot_left=True,
            has_bot_right=True,
            has_bot=True
        ),
        Digit(
            value=9,
            has_top=True,
            has_top_left=True,
            has_top_right=True,
            has_mid=True,
            has_bot_left=False,
            has_bot_right=True,
            has_bot=True
        )
    ]


def get_resize_values(init_height, init_width, target_height, target_width):
    """ Values for transforming an image via scaling and cropping """
    new_height, new_width = int(target_height), int(init_width / init_height * target_width)
    y_start, y_end = 0, -1
    x_start, x_end = int((new_width - target_width) / 2), int(new_width - (new_width - target_width) / 2)
    return new_height, new_width, y_start, y_end, x_start, x_end


def group_list_by_size(trend_list, list_size):
    # This groups any one dimensional list and groups it into lists with length of up to list_size
    if not trend_list:
        return []
    if len(trend_list) < list_size:
        return [trend_list]
    data_list_list = list([list(x) for x in zip(*[iter(trend_list)] * list_size)])
    if len(trend_list) % list_size != 0:
        data_list_list.append(trend_list[-(len(trend_list) % list_size):])
    return data_list_list

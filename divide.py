from PIL import Image
import os
from image_info import info


def divide(image_file: str, parts_dir: str, parts_amt: int, save_file: str, silent=False) -> int:
    """
    Divides image at image_file to parts_amt parts
    :param image_file: relative path to an image
    :param parts_amt: amount of parts to be divided
    :param parts_dir: where to find images
    :param save_file:
    :param silent: True if you don't want to see prints
    :return:
    """
    main_image = Image.open(image_file, mode='r')
    ways = info(image_file, silent=True)
    if len(ways) == 0:
        return -1
    selected_way = []
    for way in ways:
        if way[0] * way[1] == parts_amt:
            selected_way = way
            break
    else:
        return -1
    segments_mean_colors = [[None] * selected_way[0] for _ in range(selected_way[1])]
    main_pixels = main_image.getdata()
    x_size, y_size = main_image.size
    for y in range(y_size):
        for x in range(x_size):
            cur_pixel = main_pixels[x + y * y_size]
            segment_x = x // selected_way[0]
            segment_y = y // selected_way[1]
            if segments_mean_colors[segment_y][segment_x] is None:
                segments_mean_colors[segment_y][segment_x] = cur_pixel[:3]
            else:
                new_val = segments_mean_colors[segment_y][segment_x]
                new_val = [(new_val[i] + cur_pixel[i]) // 2 for i in range(3)]
                segments_mean_colors[segment_y][segment_x] = new_val
    print(*segments_mean_colors, sep='\n')

    # for test
    test_img = main_image.copy()
    for y in range(y_size):
        for x in range(x_size):
            segment_x = x // selected_way[0]
            segment_y = y // selected_way[1]
            cur_pixel = segments_mean_colors[segment_y][segment_x]
            test_img.putpixel((x, y), tuple(cur_pixel))

    test_img.save('test_images/image.png')


if __name__ == '__main__':
    divide('test_images/img copy.png', '/', 100, 'a')
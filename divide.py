from PIL import Image
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
        print('This image cannot be divided like this')
        return -1
    selected_way = []
    for way in ways:
        if way[0] * way[1] == parts_amt:
            selected_way = way
            break
    else:
        print('This image cannot be divided like this')
        return -1
    segments_mean_colors = [[None] * selected_way[0] for _ in range(selected_way[1])]

    x_size, y_size = main_image.size
    main_pixels = main_image.getdata()
    main_pixels = [[main_pixels[i * y_size + j] for j in range(x_size)] for i in range(y_size)]
    selected_way = [x_size // selected_way[0], y_size // selected_way[1]]
    for y in range(y_size):
        for x in range(x_size):
            cur_pixel = main_pixels[y][x]
            segment_x, segment_y = x // selected_way[0], y // selected_way[1]
            new_val = segments_mean_colors[segment_y][segment_x]
            if new_val is None:
                new_val = cur_pixel[:3]
            else:
                new_val = [(new_val[i] + cur_pixel[i]) // 2 for i in range(3)]
            segments_mean_colors[segment_y][segment_x] = new_val
    # for test
    test_img = main_image.copy()
    for y in range(y_size):
        for x in range(x_size):
            segment_x = x // selected_way[0]
            segment_y = y // selected_way[1]
            cur_pixel = segments_mean_colors[segment_y][segment_x]
            test_img.putpixel((x, y), tuple(cur_pixel))

    test_img.save('test_images/out_image.png')
    print('New image saved at test_images/out_image.png')


if __name__ == '__main__':
    divide('test_images/img_1.png', '/', 123424, 'a')

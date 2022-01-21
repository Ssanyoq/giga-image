from PIL import Image
from math import gcd


def info(image_file: str, silent=False) -> tuple:
    """
    Shows an information about given image
    :param image_file: relative path to an image
    :param silent: True if you want to print something out
    :return: None
    """

    image = Image.open(image_file, 'r')
    pixels = image.getdata()
    x_size, y_size = image.size
    g = gcd(x_size, y_size)
    if g == 1:
        if not silent:
            print(f'This image cannot be divided. (x={x_size}, y={y_size})')
        return ()
    ways = []
    for i in range(1, g + 1):
        if x_size % i == 0 and y_size % i == 0:  # if common divisor or not
            ways.append([x_size // i, y_size // i])

    if not silent:
        print(f"This image can be divided {len(ways)} different ways:")
        print(
            *[f"{way[0]}x{way[1]} ({way[0] * way[1]} parts {x_size // way[0]}x{y_size // way[1]} px)" for way in ways],
            sep='\n')
    return tuple(ways)


if __name__ == '__main__':
    info('test_images/new_img.png')

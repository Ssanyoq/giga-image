from PIL import Image


def mean_color(image_file: str) -> tuple:
    """
    A function that finds mean color of an image
    :param image_file: relative path to the image
    :return: mean color - (r, g, b)
    """
    image = Image.open(image_file, 'r')
    pixels = image.getdata()
    sums = [0, 0, 0]
    for pixel in pixels:
        r, g, b = pixel[:3]
        sums[0] += r
        sums[1] += g
        sums[2] += b
    means = tuple(i // len(pixels) for i in sums)
    return means


if __name__ == '__main__':
    print(mean_color('test_images/img.png'))  # for tests

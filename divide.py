from PIL import Image
import os


def divide(image_file: str, parts_dir: str, parts_amt: int, save_file: str) -> None:
    """
    Divides image at image_file to parts_amt parts
    :param image_file: relative path to an image
    :param parts_amt: amount of parts to be divided
    :param parts_dir: where to find images
    :param save_file:
    :return:
    """
    main_image = Image.open(image_file, mode='r')

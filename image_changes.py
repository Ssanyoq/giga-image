from PIL import Image


def resize(image_file: str, x: int, y: int, save_file: str) -> None:
    '''
    Resizes an image to X x Y size without cropping
    :param image_file: relative path to an image
    :param x: new x size
    :param y: new y size
    :param save_file: where to save a resized version
    :return: None
    '''
    image = Image.open(image_file, 'r')
    new_image = image.resize((x, y))
    new_image.save(save_file)


if __name__ == '__main__':
    resize('test_images/img.png', 35, 35, 'test_images/new_img.png')

from PIL import Image, ImageDraw, ImageFont
import os

def image_converter(basic_ext, required_ext):
    path_dir = os.getcwd()
    for file in os.listdir(path_dir):
        filename = os.path.splitext(file)
        if basic_ext == filename[1]:
            im = Image.open(file)
            im.save(filename[0] + required_ext)
        font = ImageFont.truetype("arial.ttf", size = 12)
        idraw = ImageDraw.Draw(im)
        idraw.text(xy = (im.width / 2, im.height / 2),
                   text = 'Hello,\n World!', font = ImageFont)
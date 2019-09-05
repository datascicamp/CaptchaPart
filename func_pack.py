from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random
from config import Config


# call this function to create a captcha image and its code
def create_captcha_by_code(captcha_code):
    # Image size: 130 x 50
    img_width = 130
    img_height = 50
    # create a image object
    img = Image.new('RGB', (img_width, img_height), 'white')
    # set image font
    # fc-list :lang=en (check font in this machine)
    font = ImageFont.truetype('./Andale Mono.ttf', size=40)
    # create draw
    draw = ImageDraw.Draw(img)
    draw.text((5+random.randint(4, 7)+20, 5+random.randint(3, 7)), text=captcha_code, fill='black', font=font)

    # add some lines on the image
    for num in range(8):
        x1 = random.randint(0, img_width/2)
        y1 = random.randint(0, img_height/2)
        x2 = random.randint(0, img_width)
        y2 = random.randint(img_height/2, img_height)
        draw.line(((x1, y1), (x2, y2)), fill='black', width=1)

    # image filter
    img = img.filter(ImageFilter.FIND_EDGES)
    return img


# call this function to create a captcha image and its code without giving a captcha code
def create_captcha_by_identifiers():
    # Identifiers set (a string)
    identifiers = Config.identifiers
    # Image size: 130 x 50
    img_width = 130
    img_height = 50
    # create a image object
    img = Image.new('RGB', (img_width, img_height), 'white')
    # set image font
    font = ImageFont.truetype('./Andale Mono.ttf', size=40)
    # create draw
    draw = ImageDraw.Draw(img)
    captcha_code = ''
    # print identifier one by one
    for item in range(5):
        text = random.choice(identifiers)
        captcha_code += text
        draw.text((5 + random.randint(4, 7) + 20 * item, 5 + random.randint(3, 7)), text=text, fill='black', font=font)

    # add some lines on the image
    for num in range(8):
        x1 = random.randint(0, img_width/2)
        y1 = random.randint(0, img_height/2)
        x2 = random.randint(0, img_width)
        y2 = random.randint(img_height/2, img_height)
        draw.line(((x1, y1), (x2, y2)), fill='black', width=1)

    # image filter
    img = img.filter(ImageFilter.FIND_EDGES)
    return img, captcha_code


if __name__ == '__main__':
    image, code = create_captcha_by_identifiers()
    image.save('captcha.jpeg')
    print(code)

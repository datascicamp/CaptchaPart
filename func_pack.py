from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random
from datetime import datetime, timedelta
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


# generate random code from identifiers
def generate_random_captcha_code():
    # Identifiers set (a string)
    identifiers = Config.identifiers
    captcha_code = ''
    for item in range(4):
        text = random.choice(identifiers)
        captcha_code += text
    return captcha_code


# 随机生成唯一编码
def create_random_hash():
    nowtime = datetime.now().strftime("%Y%m%d%H%M%S")
    hash_code = hash(nowtime)
    # 绝对值处理
    if hash_code < 0 :
        hash_code = str(abs(hash_code))
    else:
        hash_code = str(hash_code)
    # 再添加随机位确保哈希值不重复
    seed = "abcdef"
    title = ""
    for _ in range(6):
        title = title + random.choice(seed)
    return str(title + hash_code)


# 生成上一天日期
def get_last_date():
    now = datetime.now()
    last_datetime = now - timedelta(days=1)
    return str(last_datetime.strftime("%Y-%m-%d"))


# 生成过去某日相对此刻的 utc 时间
def get_passed_utc_date_by_seconds(seconds):
    now = datetime.utcnow()
    passed_date = now - timedelta(seconds=seconds)
    return str(passed_date)


# 生成过去某日相对此刻的 utc 时间
def get_future_utc_date_by_seconds(seconds):
    now = datetime.utcnow()
    passed_date = now + timedelta(seconds=seconds)
    return str(passed_date)


if __name__ == '__main__':
    print(get_passed_utc_date_by_seconds(600))
    pass

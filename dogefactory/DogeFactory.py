import random
from PIL import Image, ImageDraw, ImageFont
import io
import math
from dogefactory.randomDoge import randomDoge


class DogeFactory:
    def __init__(self, text, separator=';', max_attempts=1000):
        self.text = self.parse_text(text, separator)
        self.background = None
        self.prev_points = []
        self.max_attempts = max_attempts
        self.attempts = 0

    def parse_text(self, text, separator):
        if isinstance(text, str):
            for string in text.split(separator):
                yield string.strip()

    def load_image_from_bytes(self, bytes):
        stream = io.BytesIO(bytes)
        image = Image.open(stream).convert('RGBA')
        self.background = image
        return self

    def place_text(self, text, color, angle):

        assert len(color) == 4

        image_size = self.background.size
        txt = Image.new('RGBA', image_size, (255, 255, 255, 0))

        text_size = int((image_size[0] + image_size[1]) / 50)
        font = ImageFont.truetype("comic.ttf", text_size)

        d = ImageDraw.Draw(txt)
        d.text((0, -5), text, font=font, fill=color)
        w, h = d.textsize(text, font)

        coords = self.generate_coords(w)

        txt = txt.crop((0,0, w, h))
        txt1 = txt.rotate(angle, expand=True)

        txt = Image.new('RGBA', self.background.size, (255, 255, 255, 0))

        text_coords = (int(coords[0] - w/2), int(coords[1] - h/2))
        txt.paste(txt1, text_coords)

        self.background = Image.alpha_composite(self.background, txt)

        return self

    def create_doge(self):
        assert self.background is not None, 'specify background picture'

        for text_line in self.text:
            self.place_text(text_line, self.generate_color(), self.generate_angle())

        return self.background

    def generate_angle(self):
        return random.uniform(-10.0, 10.0)

    def generate_color(self):
        list = [random.randint(128, 255), random.randint(0, 64), random.randint(0, 64)]
        random.shuffle(list)
        list.append(255)
        return tuple(list)

    def generate_coords(self, text_width):
        size_w, size_h = self.background.size
        x, y = -1, -1
        half_w = text_width / 2

        while True:
            x, y = random.randint(0, size_w), random.randint(0, size_h)

            if x - half_w > 0 \
                    and x + half_w < size_w \
                    and y - half_w > 0 \
                    and y + half_w < size_h\
                    and self.check_distance(x, y, half_w):
                break

            self.attempts += 1
            if self.attempts > self.max_attempts:
                raise Exception('max attempts count exceeded')

        self.prev_points.append((x, y, half_w))
        return x, y

    def check_distance(self, x, y, half_w):
        for xp, yp, dist in self.prev_points:
            if math.sqrt((xp - x)**2 + (yp - y)**2) < half_w + dist:
                return False
        return True

if __name__ == '__main__':
    text = "Hello World;Hello World;Hello World;Hello World;Hello World;Hello World;Hello World;" \
           "Hello World;Hello World"

    background = randomDoge()

    stream

    doge = DogeFactory(text, ';')\
        .load_image_from_bytes(background)\
        .create_doge()

    doge.show()

import torchvision.transforms as transforms
from PIL import Image, ImageDraw
import random
import math
import io
from IPython.display import display, Image as IPImage


class Canvas:
    def __init__(self, width=256, height=256, color=(255, 255, 255)):
        self.width = width
        self.height = height
        self.image = Image.new("RGB", (width, height), color)
        self.draw = ImageDraw.Draw(self.image)

    def save(self, filename):
        self.image.save(filename)

    def show(self):
        # Convert PIL Image to bytes
        buf = io.BytesIO()
        self.image.save(buf, format="PNG")
        buf.seek(0)

        # Display the image in the notebook
        display(IPImage(buf.getvalue()))

    def to_tensor(self):
        # Convert PIL Image to tensor
        transform = transforms.ToTensor()
        return transform(self.image)


class Square:
    def __init__(self, x, y, s, color):
        self.x = x
        self.y = y
        self.s = s
        self.color = color

    def draw(self, canvas):
        x1 = self.x - self.s // 2
        y1 = self.y - self.s // 2
        x2 = x1 + self.s
        y2 = y1 + self.s
        canvas.draw.rectangle([x1, y1, x2, y2], fill=self.color, outline=None)


def sample_two_squares_unifrom_dist(sq_size=30, bounds=(50, 150), show=True):
    "two squares sampled with a uniform distance between them, centered in the image"
    canvas = Canvas()

    square_size = sq_size

    distance = random.uniform(*bounds)

    angle = random.uniform(0, 2 * math.pi)
    x1 = canvas.width // 2 - distance / 2 * math.cos(angle)
    y1 = canvas.height // 2 - distance / 2 * math.sin(angle)
    x2 = canvas.width // 2 + distance / 2 * math.cos(angle)
    y2 = canvas.height // 2 + distance / 2 * math.sin(angle)

    square1 = Square(int(x1), int(y1), square_size, (255, 0, 0))  # Red square
    square2 = Square(int(x2), int(y2), square_size, (0, 0, 255))  # Blue square

    square1.draw(canvas)
    square2.draw(canvas)

    tensor_image = canvas.to_tensor()
    if show:
        canvas.show()

    return tensor_image, distance

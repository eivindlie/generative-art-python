from PIL import Image, ImageDraw

_image = None
_draw = None
_foreground = None


def init(size=(1920, 1080), background='black', mode='RGB', foreground=(255, 255, 255)):
    global _image, _draw, _foreground
    _foreground = foreground
    _image = Image.new(mode, size, color=background)
    _draw = ImageDraw.Draw(_image)


def set_foreground(foreground):
    global _foreground
    _foreground = foreground


def scale_coords(coords):
    return tuple((v * _image.size[i % 2]
                  for i, v in enumerate(coords)))


def line(from_coords, to_coords, color=None):
    if not color:
        color = _foreground
    _draw.line(scale_coords(from_coords + to_coords), fill=color)


def ellipse(top_left, bottom_right, fill=-1, outline=None, width=1):
    if fill == -1:
        fill = _foreground

    _draw.ellipse(scale_coords(top_left + bottom_right), fill=fill, outline=outline, width=width)


def circle(center, radius, fill=-1, outline=None, width=1):



def show():
    _image.show()


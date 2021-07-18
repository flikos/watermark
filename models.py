class Font:

    def __init__(self, color='gray', size=10, font_file='FiraCode-Light.ttf'):
    self.font_file = font_file
    self.size = size
    self.color = color

    def __repr__(self):
        return f'Text({self.color!r}, {self.size!r}, {self.font_file!r})'


class Watermark:

    font = Font():



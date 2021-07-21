class Image:
    '''Файл для наложения водяного знака'''

    def __init__(self, filename, ):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass



class Watermark:
    '''Водяной знак'''

    def __init__(self, image_path, text='watermark', color_text='gray', start_position=(50, 50), font_ratio=1, fill_text=True, fontfile="FiraCode-Light.ttf"):
        self.text = text
        
        color_dict = {
        'black' : (0, 0, 0),
        'gray' : (128, 128, 128),
        'white' : (255,  255, 255)
        }
        self.color = color_dict.get(color_text, 'gray')


    def __enter__(self):
        pass


    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class Font:

    def __init__(self, color='gray', size=10, font_file='FiraCode-Light.ttf'):
    self.font_file = font_file
    self.size = size
    self.color = color

    def __repr__(self):
        return f'Text({self.color!r}, {self.size!r}, {self.font_file!r})'


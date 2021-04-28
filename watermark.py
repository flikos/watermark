import os
import sys

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont



def watermark_text(image_path, text='watermark', color_text='gray', startpos=(50, 50), fontfile="FiraCode-Light.ttf"):
    ''' Накладываем водяной знак на изображение.
        Необходимые параметры запуска: watermark.py imagefile
        Параметры запуска: watermark.py imagefile watermark_text color start_position fontfile
        color: 'gray', 'black', 'white'
        Пример (example):  watermark.py image.jpg 'some text' black (0,0) font.ttf
    '''

    photo = Image.open(image_path)

    # make the image editable
    drawing = ImageDraw.Draw(photo)

    color_dict = {
        'black' : (0, 0, 0),
        'gray' : (128, 128, 128),
        'white' : (255,  255, 255)
    }
    color = color_dict.get(color_text, 'gray')

    font = ImageFont.truetype(fontfile, 15)
    for x in range(startpos[0], photo.size[0], photo.size[0]//5):
        for y in range(startpos[1], photo.size[1], photo.size[1]//5):
            text_pos = (x, y)
            drawing.text(text_pos, text, fill=color, font=font)

    # photo.show()
    photo.save('wm_' + image_path)
    return 'wm_' + image_path


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(watermark_text.__doc__)

    exit()
    #for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.save(outfile)
        except OSError:
            print("cannot convert", infile)

#!/usr/bin/python3

#TODO
# Аргументы из локальной строки
# Поднять веб-сервер и обрабатывать загрузку файлов и выдачу файла в ответ
# Сделать RESTapi для внешних приложений на сайте


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os

from flask import Flask, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])
FONT_FILE = "FiraCode-Light.ttf"


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024    # Пока ограничение на загрузку 4Mb


def allowed_file(filename: str):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and  allowed_file(file.filename):
            # TODO
            # Почему подготовка имени файла идёт после проверки на допустимые файлы?
            # Не может ли быть такого случая, когда имя файла после подготовки станет недопустимым?
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('get_image', filename=filename))
            # return redirect(url_for('upload_file'))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Загрузите файл для обработки</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value="Обработать">
    </form>
    '''


@app.route('/get_image/<filename>')
def get_image(filename):
    if filename:
        return send_file(watermark_text(filename), as_attachment=True)
    return redirect(url_for('upload_file'))


def watermark_text(image_path, text='watermark', color_text='gray', startpos=(50, 50)):

    photo = Image.open(image_path)

    # make the image editable
    drawing = ImageDraw.Draw(photo)

    color_dict = {
        'black' : (0, 0, 0),
        'gray' : (128, 128, 128),
        'white' : (255,  255, 255)
    }
    color = color_dict.get(color_text, 'gray')

    font = ImageFont.truetype(FONT_FILE, 15)
    for x in range(startpos[0], photo.size[0], photo.size[0]//5):
        for y in range(startpos[1], photo.size[1], photo.size[1]//5):
            text_pos = (x, y)
            drawing.text(text_pos, text, fill=color, font=font)

    # photo.show()
    photo.save('wm_' + image_path)
    return 'wm_' + image_path

if __name__ == '__main__':

    if not os.path.exists(FONT_FILE):
        print(FONT_FILE, 'not found')

    app.run(debug=True)

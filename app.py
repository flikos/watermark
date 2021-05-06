#!/usr/bin/python3

# TODO
# Аргументы из локальной строки
# Поднять веб-сервер и обрабатывать загрузку файлов и выдачу файла в ответ
# Сделать RESTapi для внешних приложений на сайте


import os

from flask import Flask, flash, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap

import forms
import watermark


UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])
FONT_FILE = "FiraCode-Light.ttf"
SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * \
    1024    # Ограничение на загрузку 4Mb
app.config['SECRET_KEY'] = SECRET_KEY
app.config['DEBUG'] = True

bootstrap = Bootstrap(app)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    flash('Крестик не закрывает!!!')
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            # TODO
            # Почему подготовка имени файла идёт после проверки на допустимые файлы?
            # Не может ли быть такого случая, когда имя файла после подготовки станет недопустимым?
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            start_x = int(request.form['start_x']
                          ) if request.form['start_x'] else 50
            start_y = int(request.form['start_y']
                          ) if request.form['start_y'] else 50
            start_position = (start_x, start_y)
            print(start_position)
            fill_text = (request.form['fill'] == 'optionAll')
            watermark_file = watermark.watermark_text(
                filename, request.form['watermark'], startpos=start_position, fill_text=fill_text)
            return redirect(url_for('get_image', filename=watermark_file))
            # return redirect(url_for('upload_file'))
    return render_template('index.html')


@app.route('/get_image/<filename>')
def get_image(filename):
    if filename:
        return send_file(filename, as_attachment=True)
    return redirect(url_for('upload_file'))


if __name__ == '__main__':

    if not os.path.exists(FONT_FILE):
        print(FONT_FILE, 'not found')

    app.run()

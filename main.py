from flask import Flask, render_template, request
import os


PHOTOS = [
    'static/img/photo2.jpg', 'static/img/photo3.jpg']

app = Flask(__name__)


@app.route('/')
@app.route('/index/<title>')
def index(title="Заготовка"):
    return render_template('base.html', title=title)


@app.route('/galery', methods=['POST', 'GET'])
def galery():
    global PHOTOS

    if request.method == 'GET':
        return render_template('galery.html', photos=PHOTOS, length=len(PHOTOS))

    elif request.method == 'POST':
        f = request.files['file']


        if not os.getcwd().endswith('Галерея с загрузкой\static\img'):
            os.chdir('Галерея с загрузкой\static\img')
        with open(f'photo{len(PHOTOS) + 2}.jpg', 'wb') as file:
            file.write(f.read())

        PHOTOS.append(f'\static\img\photo{len(PHOTOS) + 2}.jpg')

        return render_template('galery.html', photos=PHOTOS, length=len(PHOTOS))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

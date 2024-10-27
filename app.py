from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Папки с изображениями
IMAGES_FOLDER = 'images'
AS_IMAGES_FOLDER = 'as_images'

@app.route('/')
def index():
    # Получаем список изображений из папки images
    images = os.listdir(IMAGES_FOLDER)
    return render_template('index.html', images=images)

@app.route('/as_images')
def as_index():
    # Получаем список изображений из папки as_images
    as_images = os.listdir(AS_IMAGES_FOLDER)
    return render_template('as_index.html', images=as_images)

@app.route('/images/<path:filename>')
def send_image(filename):
    return send_from_directory(IMAGES_FOLDER, filename)

@app.route('/as_images/<path:filename>')
def send_as_image(filename):
    return send_from_directory(AS_IMAGES_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)

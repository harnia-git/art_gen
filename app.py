from flask import Flask, render_template, url_for, send_from_directory
from flask_bootstrap import Bootstrap
import cv2
import base64

app = Flask(__name__)
bootstrap = Bootstrap(app)

def read_image():
    img = cv2.imread('static/lenna.jpg')  # 画像をOpenCVで読み込む
    _, buffer = cv2.imencode('.jpg', img)  # JPG形式でエンコード
    img_base64 = base64.b64encode(buffer).decode('utf-8')  # Base64エンコード
    return img_base64
# @app.route('/')
# def home():
#     return render_template('home.html')
@app.route('/')
def home():
    img_data = read_image()
    return render_template('home.html', img_data=img_data)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True) #デプロイする前にオフにする！
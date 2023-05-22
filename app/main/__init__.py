from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from entities.imgPathConf import imgPathConf

imgConf = imgPathConf()

imgConf.config['ICON'] = '/Users/feisen/Documents/hackatho_45_imgs/users_icon/'
imgConf.config['ARTICAL'] = '/Users/feisen/Documents/hackatho_45_imgs/articals/'
imgConf.config['BOOK'] = '/Users/feisen/Documents/hackatho_45_imgs/books/'
imgConf.config['PHOTO'] = '/Users/feisen/Documents/hackatho_45_imgs/photos/'


def create_app():
    return app
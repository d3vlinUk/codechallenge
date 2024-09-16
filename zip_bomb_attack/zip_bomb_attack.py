
import tarfile
from flask import Flask, request
app = Flask(__name__)


@app.route('/someUrl')
def zip_bomb_attack_noncompliant():
    file = request.files['file']
    filename = file.filename
    file.save(filename)
    tfile = tarfile.open(filename)
    tfile.extractall('./tmp/')
    tfile.close()
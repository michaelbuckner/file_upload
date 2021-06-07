from flask import Flask

UPLOAD_FOLDER = '/home/ec2-user'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DEBUG'] = True
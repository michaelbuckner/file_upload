import os
import urllib.request
from app import app
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename

@app.route('/file-upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    # if 'file' not in request.files:
    #     resp = jsonify({'message' : 'No file part in the request'})
    #     resp.status_code = 400
    #     return resp
    # file = request.files['file']
    # if file.filename == '':
    #     resp = jsonify({'message' : 'No file selected for uploading'})
    #     resp.status_code = 400
    #     return resp
    # if file:
    #     filename = secure_filename(file.filename)
    #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #     resp = jsonify({'message' : 'File successfully uploaded'})
    #     resp.status_code = 201
    #     return resp
    # else:
    #     resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
    #     resp.status_code = 400
    #     return request
    print(request)
if __name__ == "__main__":
    app.run(host='0.0.0.0')

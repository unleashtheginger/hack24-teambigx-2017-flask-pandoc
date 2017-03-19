# Taken from http://flask.pocoo.org/docs/0.12/patterns/fileuploads/

import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/tmp/uploaded_files/'
ALLOWED_EXTENSIONS = set(['md', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "ODSFDSFDSFHDSFHDSAFSAK"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def show_index():
    return ""

@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print "POST"
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            print "No file part"
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print "No selected file"
            flash('No selected file')
            return redirect(request.url)
        print allowed_file(file.filename)
        if file and allowed_file(file.filename):
            print "attempting to upload file?"
            filename = secure_filename(file.filename)
            print filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print "allegedly uploaded file"
            return redirect('/')
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)

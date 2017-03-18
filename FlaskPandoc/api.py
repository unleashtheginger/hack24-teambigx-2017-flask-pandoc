from flask import Flask, flash, request, redirect, url_for
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename
import ConvertPandoc
import os

UPLOAD_FOLDER = '/tmp/uploaded_files/'
OUTPUT_FOLDER = '/tmp/output_files/'
ALLOWED_EXTENSIONS = set(['md'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "lolz"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/pandoc/<filename>', methods=['GET'])
def show_index(filename):
    input_file_path = UPLOAD_FOLDER + filename
    output_file_path = OUTPUT_FOLDER + filename
    output_file_path = output_file_path.rsplit( ".", 1 )[ 0 ]
    output_file_path = output_file_path + ".docx"

    if not os.path.isfile(input_file_path):
        return "file not uploaded"
    pandoc = ConvertPandoc.ConvertPandoc(input_file_path, output_file_path)
    if not pandoc:
        return "problem converting. Check debug log!"
    
    success = pandoc.convert()
    return_value = (output_file_path, success)
    return str(return_value)

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
            return """File uploaded"""
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


from flask import Flask, request, redirect, url_for
import os
app = Flask(__name__)


UPLOAD_FOLDER = '/Users/sandeepanghosh/Downloads/flaskr'
#sotres the files in this location
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        filename = request.files['file']
        if filename.filename.rsplit(".",1)[1]=='pdf':
            filename.save(os.path.join(app.config['UPLOAD_FOLDER'], filename.filename ))
            return "Succesly uploaded"
        else:
            print("Invalid format")
            return redirect(request.url)
    return '''
     <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit">
    </form>
    '''
 
  

if __name__ == '__main__':
 app.run(debug=True)

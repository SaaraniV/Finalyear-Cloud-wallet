from flask import Flask,render_template,url_for, request, jsonify,redirect
import os
app = Flask("__name__")

@app.route('/')
def index():
    os.remove('./uploads/messi-gif.gif') 
    return render_template('index.html')

@app.route('/upload',methods=['POST','GET'])
def upload():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file:
        destination_folder = './uploads'
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        file = request.files['file']
        filename = os.path.join(destination_folder,file.filename)
        file.save(filename)
        return "uploaded"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)
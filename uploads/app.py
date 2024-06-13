from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')
    
@app.route('/uploadFile', methods=["POST"])
def uploadFile():
    
    if "file" not in request.files:
        return "Please select a file"
    
    file = request.files['file']
    file_size = request.content_length
    
    if file.filename == '':
        return "File not selected"
    
    if file_size > 1048576:
        return "File size is too big. Upload file smaller in size"
    
    def savefile(file):
        file.save("uploads/" + file.filename)
        return "File uploaded successfully"
    
    result = savefile(file)
    return result

if __name__ == '__main__':
    app.run()
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')
    
@app.route('/uploadFile', methods=["POST"])
def uploadFile():
    try:
        if "file" not in request.files:
            return "Please select a file"

        file = request.files['file']
        if file.filename == '':
            return "File not selected"

        file_size = request.content_length
        if file_size > 1048576:
            return "File size is too big. Upload file smaller in size"

        # Ensure 'uploads' directory exists
        uploads_dir = os.path.join(os.getcwd(), 'uploads')
        os.makedirs(uploads_dir, exist_ok=True)

        # Save file
        file.save(os.path.join(uploads_dir, file.filename))
        
        return "File uploaded successfully"

    except Exception as e:
        app.logger.error(f"Error uploading file: {str(e)}")
        return "Internal Server Error", 500

if __name__ == '__main__':
    app.run()

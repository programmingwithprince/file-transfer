from flask import Flask, request, render_template,send_from_directory
import os, json,webbrowser

app = Flask(__name__)
file_path="uploads"
# Set the folder where you want to store the uploaded files
app.config['UPLOAD_FOLDER'] = 'uploads'
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['file']
    if f:
        f.save(f"uploads/{f.filename}")
        return 'File uploaded successfully.'
    else:
        return 'No file uploaded.'


@app.route('/get_urls')
def send_url():
    files=os.listdir("uploads")
    return files


@app.route('/download/<filename>',methods=['GET'])
def download(filename):
    #return render_template('index.html')
    # Use send_from_directory to serve the file
    return send_from_directory('uploads',filename, as_attachment=True)    
    
            
if __name__ == '__main__':
    webbrowser.open('http://localhost:5000')
    app.run(debug=True,host="0.0.0.0")       
from flask import Flask, request, jsonify, render_template_string
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
ALLOWED_EXTENSIONS = {'mp3', 'ogg', 'wav'}

# HTML template for file upload and list display
HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Sound Files</title>
</head>
<body>
    <h1>Uploaded Sound Files</h1>
    <ul>
    {% for file in files %}
        <li>{{ file }}</li>
    {% endfor %}
    </ul>

    <h2>Upload a new sound file</h2>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>

    {% if error %}
        <p style="color:red;">{{ error }}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    # List all files in the upload folder
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template_string(HTML_TEMPLATE, files=files, error=None)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify(error='No file part'), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify(error='No selected file'), 400
    if not allowed_file(file.filename):
        return render_template_string(HTML_TEMPLATE, files=os.listdir(app.config['UPLOAD_FOLDER']), error="Non-audio file detected"), 400
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template_string(HTML_TEMPLATE, files=os.listdir(app.config['UPLOAD_FOLDER']), error=None)

@app.route('/list', methods=['GET'])
def list_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return jsonify(files=files), 200

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(port=8888)

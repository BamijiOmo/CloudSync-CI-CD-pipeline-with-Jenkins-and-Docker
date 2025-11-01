from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return '☁️ CloudSync backend is live — CI/CD pipeline initialized.'

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(f"./uploads/{file.filename}")
    return f"File {file.filename} uploaded successfully."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


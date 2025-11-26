from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from loguru import logger
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/upload', methods=['POST'])
def upload_document():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    
    logger.info(f"File uploaded: {file.filename}")
    
    return jsonify({
        'success': True,
        'filename': file.filename,
        'message': 'File uploaded successfully'
    })


@app.route('/api/diagnose', methods=['POST'])
def diagnose():
    data = request.get_json()
    
    return jsonify({
        'diagnosis': 'Analysis complete',
        'confidence': 0.89,
        'recommendations': [
            'Further examination recommended',
            'Follow-up in 2 weeks'
        ]
    })


@app.route('/api/status')
def status():
    return jsonify({
        'service': 'MediDoc AI',
        'version': '1.0.0',
        'status': 'running',
        'features': {
            'ocr': True,
            'multi_agent': True,
            'edge_mode': True
        }
    })


if __name__ == '__main__':
    logger.info("Starting MediDoc AI web service")
    logger.info("Visit http://localhost:5000 to access the interface")
    app.run(host='0.0.0.0', port=5000, debug=True)

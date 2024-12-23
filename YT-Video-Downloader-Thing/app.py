from flask import Flask, request, jsonify, send_file, render_template
from downloader import download_video, download_subtitles
import os

app = Flask(__name__)
DOWNLOAD_PATH = 'downloads'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        result = download_video(url, output_path=DOWNLOAD_PATH)
        filename = os.listdir(DOWNLOAD_PATH)[0]  # Assuming single file downloaded
        return jsonify({'message': 'Video ready', 'filename': filename})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/subtitles', methods=['POST'])
def subtitles():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        result = download_subtitles(url, output_path=DOWNLOAD_PATH)
        filename = os.listdir(DOWNLOAD_PATH)[0]  # Assuming single file downloaded
        return jsonify({'message': 'Subtitles ready', 'filename': filename})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download-file/<filename>')
def download_file(filename):
    try:
        file_path = os.path.join(DOWNLOAD_PATH, filename)
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    os.makedirs(DOWNLOAD_PATH, exist_ok=True)
    app.run(host='0.0.0.0', port=5000)

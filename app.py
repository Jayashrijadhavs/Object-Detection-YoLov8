from flask import Flask, jsonify, request
#from flask_ngrok import run_with_ngrok
import json
from video_analysis import process_video, generate_copywriting

app = Flask(__name__)
#run_with_ngrok(app)
@app.route('/')
def index():
    return "Welcome to the Object Detection and Copywriting Service!"

@app.route('/analyze_video', methods=['POST'])
def analyze_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video file part'}), 400
    
    file = request.files['video']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    file_path = 'data/traffic.mp4'
    file.save(file_path)

    detected_objects = process_video(file_path,model)
    copywriting = generate_copywriting(detected_objects)

    response = {
        'detections': detected_objects,
        'copywriting': copywriting
    }
    
    return jsonify(response)
if __name__ == '__main__':
    app.run()

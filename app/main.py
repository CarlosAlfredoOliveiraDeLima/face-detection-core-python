import cv2
from flask import Flask, request, jsonify
import base64
import numpy as np
import cv2 as cv

app = Flask(__name__)


@app.route('/process-image', methods=['POST'])
def process_image():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data received'}), 400

        image_data = base64.b64decode(data['image'])

        nparr = np.frombuffer(image_data, np.uint8)

        image = cv.imdecode(nparr, cv.IMREAD_COLOR)

        if image is None:
            return jsonify({'error': 'Failed to decode image'}), 400



        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run()

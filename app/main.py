from flask import Flask, request, jsonify
import base64
import numpy as np
import cv2 as cv
from app.ml_utils.face_detection import face_detection


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

        faces_identified, number_faces_found = face_detection(image)

        if image is None:
            return jsonify({'error': 'Failed to decode image'}), 400

        # For testing de API with Postman and showing the image on a window
        # cv.imshow('image', faces_identified)
        # cv.waitKey(0)

        _, buffer = cv.imencode('.jpg', faces_identified)
        processed_image_base64 = base64.b64encode(buffer).decode('utf-8')

        return jsonify({
            'success': True,
            'processed_image': processed_image_base64,
            'format': 'jpeg',
            'faces_count': number_faces_found
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run()

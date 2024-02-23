from flask import Flask, send_from_directory, render_template, jsonify
import cv2
import os
from gradio_client import Client
import time
app = Flask(__name__)

#============CAMERA PART===============================#

# Directory to save images
IMAGE_DIR = './main/static/images'

# Ensure the directory exists
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

def capture_image():
    # Initialize the camera (use  0 for the default camera)
    cap = cv2.VideoCapture(3)

    # Check if the camera is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open camera")

    # Capture a single frame
    ret, frame = cap.read()

    # Release the camera
    cap.release()

    if ret:
        # Save the image
        path = f"image_{int(time.time())}.jpg"
        filename = os.path.join(IMAGE_DIR, path)
        cv2.imwrite(filename, frame)
        print(f"Image saved to {filename}")
    else:
        print("Failed to capture image")

    return path


def process_image(path):
    client = Client(
        "https://ybelkada-llava-1-5-dlai.hf.space/--replicas/f3edg/")
    result = client.predict(
        "Describe this image",  # str  in 'parameter_0' Textbox component
        path,  # filepath  in 'parameter_1' Image component
        api_name="/predict"
    )
    print(result)
    return result

@app.route('/capture')
def capture_and_save():
    path = capture_image()
    path = './main/static/images/'+path
    print(path)
    desc = process_image(path)
    # return desc
    return jsonify({'image_url': path, 'description': desc})

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/get_car_data')
# def get_car_data():
#     # Example data
#     image_url = 'static/images/image_1708585084.jpg'
#     description = 'This is a description of the car.'
    
#     # Return the data as JSON
#     return jsonify({'image_url': image_url, 'description': description})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
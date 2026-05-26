import time
from io import BytesIO
import requests
from gpiozero import Button
from picamera2 import Picamera2



# Config
SERVER_URL = "http://100.119.162.122:5000/upload"
BUTTON_GPIO = 23

# Set up the camera.
picam2 = Picamera2()
config = picam2.create_still_configuration()
picam2.configure(config)
picam2.start()

# Wait for the camera to start.
time.sleep(2)

# Set up button.
button = Button(BUTTON_GPIO)


def capture_and_upload():

    buffer = BytesIO()

    # Capture JPEG directly into RAM
    picam2.capture_file(buffer, format="jpeg")

    buffer.seek(0)

    print("Uploading image")

    response = requests.post(
        SERVER_URL,
        files={"image": ("photo.jpg", buffer, "image/jpeg")})

    print(response.json())


while True:

    button.wait_for_press()
    capture_and_upload()

    time.sleep(0.5)

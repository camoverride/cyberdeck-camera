import os
import time
from flask import Flask, request, send_file
from pathlib import Path



# Set the display to be local in case this is started via ssh.
os.environ["DISPLAY"] = ":0"
print(os.environ["DISPLAY"])
time.sleep(1)

# Config and boilerplate.
UPLOAD_FILE = Path("latest.jpg")
app = Flask(__name__)

# Upload Endpoint
@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["image"]

    file.save(UPLOAD_FILE)

    print("Image received")

    return {"status": "ok"}


# Browser page.
@app.route("/")
def index():

    return """
    <html>

    <head>
        <title>cyberdeck-camera</title>
    </head>

    <body style="background:#111;color:white;text-align:center;">

        <h1></h1>

        <img id="img"
             src="/latest.jpg"
             width="800">

        <script>

        setInterval(() => {

            document.getElementById("img").src =
                "/latest.jpg?t=" + new Date().getTime();

        }, 1000);

        </script>

    </body>
    </html>
    """


# Serve the image.
@app.route("/latest.jpg")
def latest_image():

    if not UPLOAD_FILE.exists():
        return "No image yet", 404

    return send_file(
        UPLOAD_FILE,
        mimetype="image/jpeg")



if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000)

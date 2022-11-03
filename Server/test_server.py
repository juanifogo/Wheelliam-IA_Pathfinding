from flask import Flask,request 
import cv2
from PIL import Image
import numpy as np
app = Flask(__name__)

@app.route("/test",  methods=["POST"])
def test():
    file = (request.files['data'])
    im = Image.open(file)
    im.show()
    return "200 OK"

app.run("localhost",5000)

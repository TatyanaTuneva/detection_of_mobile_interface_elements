import os
import numpy as np


from io import BytesIO
from PIL import Image
from ultralytics import YOLO


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

model = YOLO(os.path.join(ROOT_DIR, 'model.pt'))


def predict(image: BytesIO) -> bytes:
    np_image = np.asarray(Image.open(image))

    results = model(np_image)

    result_image = Image.fromarray(results[0].plot())

    image_bytes = BytesIO()
    result_image.save(image_bytes, format='PNG')

    return image_bytes.getvalue()

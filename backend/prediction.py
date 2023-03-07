import os
import numpy as np


from io import BytesIO
from PIL import Image
from ultralytics import YOLO


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

model = YOLO(os.path.join(ROOT_DIR, 'model.pt'))


def predict(image: BytesIO) -> (bytes, float):
    np_image = np.asarray(Image.open(image))

    results = model(np_image)[0]

    time = round(sum(results.speed.values()), 3)

    result_image = Image.fromarray(results.plot())

    image_bytes = BytesIO()
    result_image.save(image_bytes, format='PNG')

    return image_bytes.getvalue(), time

import io
import os
from fastapi import FastAPI, UploadFile
from fastapi.params import File
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response, FileResponse
from prediction import predict

app = FastAPI()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post(
    "/get_prediction/",
    status_code=201,
    responses={
        200: {
            "content": {"image/png": {}}
        }
    },
    response_class=Response,
)
async def get_prediction(image: UploadFile = File(...)) -> Response:
    request_object_content = await image.read()
    img = io.BytesIO(request_object_content)
    prediction = predict(img)

    return Response(content=prediction, media_type="image/png")



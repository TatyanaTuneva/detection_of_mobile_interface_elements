import io
import os
from fastapi import FastAPI, UploadFile
from fastapi.params import File
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response, FileResponse
from starlette.staticfiles import StaticFiles

from prediction import predict
import uvicorn

app = FastAPI()

app.mount("/frontend", StaticFiles(directory="frontend"), name="static")

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

TIME = 0


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
    global TIME
    prediction, TIME = predict(img)
    return Response(content=prediction, media_type="image/png")


@app.get(
    "/get_time/",
    status_code=200,
)
async def get_time() -> dict:
    return {'time': TIME}


if __name__ == '__main__':
    uvicorn.run("app.main:app",
                host="0.0.0.0",
                port=8432,
                reload=True,
                ssl_keyfile="./key.pem",
                ssl_certfile="./cert.pem"
                )
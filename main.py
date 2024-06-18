from fastapi import FastAPI, File, UploadFile
from predict import onnxPred
import uvicorn
import cv2
import os

app = FastAPI()

uploads_dir = 'uploads'
if not os.path.exists(uploads_dir):
    os.makedirs(uploads_dir)

@app.post("/predict")
def upload(file: UploadFile = File(...)):
    try:
        local_image_path = f"uploads/{file.filename}"
        with open(local_image_path, 'wb') as f:
            f.write(file.file.read())

        img = cv2.imread(local_image_path)
        result = onnxPred(img)

        return  result

    except Exception as e:
        return {"message": f"There was an error: {str(e)}"}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
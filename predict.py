import onnxruntime as rt
import numpy as np
import cv2

LABEL = ["Dog", "Cat"]
session = rt.InferenceSession('./models/cats_vs_dogs_model.onnx')

input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name

async def onnxPred(input : np.ndarray):  # Use async def
    test = cv2.resize(input, (224, 224)).astype(np.float32)
    test = np.expand_dims(test, axis=0)
    res = session.run([output_name], {input_name : test})
    return LABEL[np.argmax(res)]


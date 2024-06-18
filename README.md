# Onnx Deploy App
This project provides a simple REST API for classifying images as cats or dogs using a pre-trained ONNX model. It's built with the following technologies:

# Backend: Python (FastAPI, onnxruntime, OpenCV)
API Server: uvicorn

Dependency Management: pip

(Optional) Tunneling: ngrok (for exposing the API locally)

Features

Upload an image file.

Receive a classification response ("Cat" or "Dog").

# Running the Project

Prerequisites:

* Python 3.x
* pip (Python package manager)
* OpenCV
* onnxruntime
* uvicorn
* ngrok

# Installation:

Clone this repository:

```
https://github.com/Nurik1002/OnnxDeploy.git
```

Install dependencies:

```
pip install -r requirements.txt
```

(Optional) Install ngrok for local testing of the API from your machine. Follow ngrok's installation instructions: https://ngrok.com/download

Download a pre-trained cats vs. dogs ONNX model (.onnx file) and place it in the models directory.

Start the API:

Navigate to the project directory.

Run the API servers:

```
uvicorn main:app --host 0.0.0.0 --port 8080
```

```
ngrok http http://localhost:8080
```

Using the API:
```
import requests

def predict_image(image_path, api_url):
    api_url += "/predict"
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
    files = {'file': ('image.jpg', image_data, 'image/jpeg')}  # Key changed to 'file'

    response = requests.post(api_url, files=files)
    if response.status_code == 200:
        return response.json()
    else:
        return {'message': f"Error: {response.status_code} - {response.text}"}

```



# Testing Performance:

The script check.py demonstrates how to send multiple requests to the API and measure the total execution time. You can adjust the number of requests (n) in the script.

```
python3 check.py 
```

# Note:

This project uses a sample trained model. The model's accuracy may vary depending on the quality and diversity of the images used for testing.

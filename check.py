import requests
import time
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

if __name__=="__main__":
    start_time = time.time()
    api_url = input("NGROK API URL >>> ")  # NGROK API
    n = int(input("Num of requests >>> ")) # NUM OF REQUESTS
    for i in range(1, n+1):
        peet = "dog" if i % 2 == 0 else "cat"
        image_path = f"./images/{peet}.jpeg"
        result = predict_image(image_path, api_url)
        print(f"Test {i} result : {result}")

    end_time = time.time()
    total_time = end_time - start_time
    print(f"\nTotal execution time: {total_time:.2f} seconds")

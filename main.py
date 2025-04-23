from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
import random

app = FastAPI()

# Replace this with the absolute path to your folder
IMAGE_FOLDER = "images"

@app.get("/random-image")
def get_random_image():
    files = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    if not files:
        return {"error": "No images found."}
    random_file = random.choice(files)
    file_path = os.path.join(IMAGE_FOLDER, random_file)
    return FileResponse(path=file_path, media_type="image/jpeg")

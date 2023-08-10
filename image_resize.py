from PIL import Image
import os

input_folder = "/image_folder/"
output_folder = "/output_folder/"
target_size = (320, 240)

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img = Image.open(os.path.join(input_folder, filename))
        img = img.resize(target_size, Image.LANCZOS)
        img.save(os.path.join(output_folder, filename))

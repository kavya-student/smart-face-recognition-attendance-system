import cv2
import os
import numpy as np
from PIL import Image

dataset_path = "dataset"

faces = []
ids = []
name_to_id = {}
current_id = 0

# Loop through dataset images
for image_name in os.listdir(dataset_path):
    path = os.path.join(dataset_path, image_name)

    # Skip folders and non-image files
    if not os.path.isfile(path):
        continue

    if not image_name.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue

    # Convert image to grayscale
    gray_img = Image.open(path).convert('L')
    img_numpy = np.array(gray_img, 'uint8')

    # Extract name from filename (User.name.number.jpg)
    name = image_name.split('.')[1]

    # Assign ID if new person
    if name not in name_to_id:
        name_to_id[name] = current_id
        current_id += 1

    id = name_to_id[name]

    faces.append(img_numpy)
    ids.append(id)


if len(faces) == 0:
    print("No images found in dataset folder!")
    exit()

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(ids))

if not os.path.exists("trainer"):
    os.makedirs("trainer")

recognizer.save("trainer/trainer.yml")
with open("labels.txt", "w") as f:
    for name, id in name_to_id.items():
        f.write(f"{id},{name}\n")

print("Training Complete!")
print("Labels saved in labels.txt")
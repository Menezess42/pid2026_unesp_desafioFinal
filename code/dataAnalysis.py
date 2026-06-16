import kagglehub
from pathlib import Path
import random
import os
from PIL import Image
import plotly.express as px
from pprint import pprint
import cv2 as cv
from matplotlib import pyplot as plt

# Dataset path

DATASET_PATH = kagglehub.dataset_download(
    "andrewmvd/lung-and-colon-cancer-histopathological-images",
    output_dir="./dataset"
)

# Dataset folder structure
datapath = Path(DATASET_PATH+"/lung_colon_image_set")

dataClasses_path = [y for x in datapath.iterdir() if x.is_dir() for y in x.iterdir()]

random_class_image = [random.choice(os.listdir(str(class_path))) for class_path in dataClasses_path]


for image_path, class_name in zip(random_class_image, dataClasses_path):
    image_full_path = Path(class_name) / image_path
    class_name = str(class_name).split('/')[-1]
    img = Image.open(image_full_path)
    fig = px.imshow(img, title=f"{class_name}")
    fig.show()


path_colon_normal, path_lung_normal = dataClasses_path[1], dataClasses_path[3]

print(path_colon_normal)
print(path_lung_normal)


# Vamos pegar 5 imagens aleatórias (de cada classe) para usar.

# Devo setar random para uma seed para que eu possa sempre escolher as mesmas 5 imagens das duas classes
random.seed(42)
colon_normal_5imgs = [random.choice(list(path_colon_normal.iterdir())) for _ in range(5)]
lung_normal_5imgs = [random.choice(list(path_lung_normal.iterdir())) for _ in range(5)]

pprint(colon_normal_5imgs)
print("-----------------")
pprint(lung_normal_5imgs)


# Agora devo converter as 5 imagens colon_normal de RGB para HSV
test_img = cv.imread(colon_normal_5imgs[0])
#cv.imshow('rgb', test_img)
plt.imshow(test_img)
test_img = cv.cvtColor(test_img, cv.COLOR_BGR2HSV)
#cv.imshow('hsv', test_img)
plt.imshow(test_img)

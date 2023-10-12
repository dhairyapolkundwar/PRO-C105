import os
import cv2

path = 'images'
images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.png', '.jpeg', '.jfif', '.jpg']:
        images.append(path + '/' + file)
        

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)
fps = 0.5

videoWrite = cv2.VideoWriter("Project Output.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
for i in range(0, len(images), 1):
    frame = cv2.imread(images[i])
    videoWrite.write(frame)

videoWrite.release()
print("Done!")
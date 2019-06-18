import os

folders = ['bbox_txt', 'images']
img_path = os.path.abspath("darknet/data/obj")

img_list = os.listdir('images')
with open(f'{img_path}/train.txt', 'w') as outfile:
    for img in img_list:
        img_path_full = f"{img_path}/{img}\n"
        outfile.write(img_path_full)

for folder in folders:
    n = 0
    for file in os.scandir(folder):
        n += 1
        os.rename(file.path, os.path.join(img_path, file.name))

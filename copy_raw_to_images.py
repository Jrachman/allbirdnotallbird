from shutil import copyfile
import os

folder = 'raw_images/shoes'
path = 'images'

for image in os.scandir(folder):
    copyfile(image.path, os.path.join(path, image.name))

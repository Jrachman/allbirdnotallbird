from shutil import copyfile
import os

object_name = "shoes"
folder = f'raw_images/{object_name}'
path = 'images'

for image in os.scandir(folder):
    copyfile(image.path, os.path.join(path, f'{image.name:06}.jpg'))

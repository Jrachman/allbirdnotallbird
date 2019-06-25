import shutil
import os

# make an argsparser option here
object_name = "shoes"
folder = f'raw_images/{object_name}'
path = 'images'

for image in os.scandir(folder):
    shutil.copy(image.path, os.path.join(path, image.name))

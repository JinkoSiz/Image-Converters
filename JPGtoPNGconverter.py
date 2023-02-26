import sys
import os
from PIL import Image

# grab the first and second args

img_folder = sys.argv[1]
new = sys.argv[2]

# check if new folder exists and create


def is_exists(folder):
    if os.path.exists(folder):
        print('This folder already exists!')
        return 0
    else:
        os.makedirs(folder)
        print('Folder created!')
        return 1


# loop through img_folder and convert images
# save them to the new folder

if is_exists(new):
    img_folder_directory = os.scandir(img_folder)
    for files in img_folder_directory:
        if files:
            file_name = os.path.basename(files)
            img = Image.open(f'./{img_folder}/{file_name}')
            new_file_name = file_name.replace('.jpg', '.png')
            img.save(f'./{new}/{new_file_name}')
    print('Job done!')

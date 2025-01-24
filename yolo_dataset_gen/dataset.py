# Rename images and labels automatically

import os
import shutil
import re

def get_number(name):
    num = re.search('\d+', name)
    if num:
        return int(num.group())
    else:
        return 0


# Input
image_file_path = '/home/qingbao/Data/Dataset/car/images'
label_file_path = '/home/qingbao/Data/Dataset/car/labels'
image_files_unsorted = os.listdir(image_file_path)
image_files = sorted(image_files_unsorted, key=get_number)

print(image_files)
# output
# out_file_path = '/home/qingbao/Data/Dataset/car/labels2'

for i, file in enumerate(image_files):
    old_name, ext = os.path.splitext(file)
    new_image_name = image_file_path + '/' + str(i) + ext
    old_image_name = image_file_path + '/' + file

    old_label_name = label_file_path + '/' + old_name + '.txt'
    new_label_name = label_file_path + '/' + str(i) + '.txt'

    # print(old_image_name, '->', new_image_name)
    try:
        os.rename(old_image_name, new_image_name)
        os.rename(old_label_name, new_label_name)
        # shutil.move(old_full_name, new_full_name)
    except FileExistsError:
        print(f"{file} already exists")
    except FileNotFoundError:
        print(f"{file} not found")

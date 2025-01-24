import os
import re
import shutil

def get_number(name):
    num = re.search('\d+', name)
    if num:
        return int(num.group())
    else:
        return 0
# Input
input_file_path='/home/qingbao/Data/Dataset/car/labels'
input_files = os.listdir(input_file_path)
input_files = sorted(input_files, key=get_number)

# output
out_file_path = '/home/qingbao/Data/Dataset/car/labels2'

for i, file in enumerate(input_files):
    old_name, ext = os.path.splitext(file)
    new_full_name = out_file_path + '/' + str(i) + ext
    old_full_name = input_file_path + '/' + file
    print(old_full_name)
    # print(ext)
    # print(new_full_name)
    try:
        # os.rename(file, new_full_name)
        shutil.move(old_full_name, new_full_name)
    except FileExistsError:
        print(f"{file} already exists")
    except FileNotFoundError:
        print(f"{file} not found")



'''
Homework creator for sketching.
[Finds n random images in n folders picked at random.]
Inputs days to study, number of images per day.
Returns a homework directory with random images.
Email: sfeigen@live.com
'''
import os
import random
from shutil import copyfile

NEW_IMAGES_PATH = ''    #eg: r'C:\Root\Homework\Day_'

RANDOM_FOLDERS_1 = ''   #eg: "C:\\Root\\RandomFolders"
RANDOM_FOLDERS_2 = ''   #eg: r'C:\Root\RandomFolders'

def create_day(i):
    '''folder day in, folder day path out'''
    newpath = NEW_IMAGES_PATH+str(i)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath

def get_folder():
    '''returns path of random folder'''
    folder = random.choice(os.listdir(RANDOM_FOLDERS_1)) # random folder
    path = RANDOM_FOLDERS_2 + "\\" + folder
    return path

def get_file():
    '''returns file name, file path'''
    folder = get_folder()
    file = random.choice(os.listdir(folder))
    path = folder + "\\" + file
    return (file, path)

def copy_file(days, files):
    '''copies file to folder'''
    file = ""
    moved_images = []
    for day in range(days):
        day_path = create_day(day+1)
        while len(moved_images) < files:
            file, path = get_file()
            if file not in moved_images:
                copyfile(path, day_path + "\\" + file)
                moved_images.append(file)
            else:
                print("Duplicate Detected")
        moved_images = []

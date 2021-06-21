
import os
import glob
from glob import glob
from PIL import Image
from tqdm import tqdm
import cv2

def get_all_file_paths(directory):

    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    print("get all file paths")
    for root, directories, files in tqdm(os.walk(directory)):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    # returning all file paths
    return file_paths

def main():

    path = 'H:/Downloads/archive/lgg-mri-segmentation/kaggle_3m/*/*_mask*'
    dir = 'H:/Downloads/archive/lgg-mri-segmentation/kaggle_3m'

    #img_mask_path = os.path.join(path,'/*')
    mask_file = glob(path)
    #mask_file = glob.glob(img_mask_path+'/*_mask*',recursive=True)

    img_file = []
    for i in mask_file:
        img_file.append(i.replace('_mask',''))
    
    #print(mask_file)
    #print(img_file)

    print("create folder copied")
    if ~ os.path.exists(dir+'/Images'):
        os.mkdir(os.path.join(dir,'Images'))
        os.mkdir(os.path.join(dir,'Ground-truths'))

    #file_paths = get_all_file_paths(directory)

    #file_list = glob.glob(os.path.join(os.getcwd(), "FolderName", "*.txt"))

    #corpus = []

    #for file_path in img_file:
    #    with open(file_path) as f_input:
     #       corpus.append(f_input.read())
    
    # get file name 
    # file_name = os.path.basename(path_file)

    #corpus = [open(file).read() for file in img_file]

    #print(corpus)
    print("copied images to /Images")
    for img in tqdm(img_file):
        image = cv2.imread(img)
        file_name = os.path.basename(img)
        Image.fromarray(image).save(os.path.join(dir,'Images',file_name))
    
    print("copied masks to /Ground-truths")
    for img in tqdm(mask_file):
        image = cv2.imread(img)
        file_name = os.path.basename(img)
        Image.fromarray(image).save(os.path.join(dir,'Ground-truths',file_name))

if __name__ == '__main__':
    dir = 'H:/Downloads/archive/lgg-mri-segmentation/kaggle_3m/Ground-truths/TCGA_CS_5393_19990606_19_mask.tif'
    image = cv2.imread(dir,0)
    if cv2.countNonZero(image) == 0:
        print("black")
    #main()
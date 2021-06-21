
import os
import glob
from glob import glob
from PIL import Image
from tqdm import tqdm
import cv2

def main():

    path = 'H:/Downloads/archive/lgg-mri-segmentation/kaggle_3m/*/*_mask*'
    dir = 'H:/Downloads/archive/lgg-mri-segmentation/kaggle_3m'

    # get path all mask
    mask_file = glob(path)

    img_file = []
    # get path all image
    for i in mask_file:
        img_file.append(i.replace('_mask',''))
    
    #print(mask_file)
    #print(img_file)

    # create folder copied
    print("create folder copied")
    if ~ os.path.exists(dir+'/Images'):
        os.mkdir(os.path.join(dir,'Images'))
        os.mkdir(os.path.join(dir,'Ground-truths'))
     
    # copied images to /Images
    print("copied images to /Images")
    for img in tqdm(img_file):
        image = cv2.imread(img)
        # get file name
        file_name = os.path.basename(img)
        # save image to /Images
        Image.fromarray(image).save(os.path.join(dir,'Images',file_name))
    
    # copied masks to /Ground-truths
    print("copied masks to /Ground-truths")
    for img in tqdm(mask_file):
        image = cv2.imread(img)
        # get file name
        file_name = os.path.basename(img)
        # save image to /Images
        Image.fromarray(image).save(os.path.join(dir,'Ground-truths',file_name))

if __name__ == '__main__':

    main()
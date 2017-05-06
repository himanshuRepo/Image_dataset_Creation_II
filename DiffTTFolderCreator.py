# -*- coding: utf-8 -*-
"""
Created on Mon May  5 2017

@author: Himanshu Mittal 

This file is code by Himanshu Mittal, himanshu.mittal224@gmail.com
Purpose: Creating training and testing dataset containing images
            taken randomly from source folder(: 101_ObjectCategories).


            The source folder contains images in different categories(as sub-folders). The training and testing dataset is 
                created for each category where each category has images in 70:30 ratio.
            This code and image source folder must be in same folder.
            Command to run this code:
                python DiffTTFolderCreator.py --data_path 101_ObjectCategories

Code compatible:
 -- Python: 2.* or 3.*
"""

import argparse
from glob import glob
import numpy
import random, os
import shutil

parser = argparse.ArgumentParser(description=" Shuffled training and testing image folder creator.")
parser.add_argument('--data_path', action="store", dest="data_path", required=True)
args =  vars(parser.parse_args())

data_path = args['data_path'] 
# print data_path

# Defining the train and test data Ratio
no_train = 70
no_test = 30

for each in glob(data_path + "/*"):
    word = each.split("/")[-1]
    print " **** Reading image category ", word, " **** "
    count = 0

    # counting the number of images in each folder
    for imagefile in glob(data_path+"/"+word+"/*"):
        count +=1 
    print count

    # Defining number of training and testing images for a particular category
    train = int(numpy.floor(float(no_train*count)/100))
    test = int(numpy.floor(float(no_test*count)/100))+1

    # Reading all the filenames in a directory
    l = os.listdir(data_path+"/"+word)
    random.shuffle(l)
    # print l

    # Defining path of the source folder
    srcdir=data_path+"/"+word

    # Copying the images from source folder to training and testing folder
    traincount = 0
    for imagefile in l:
        if traincount < train:
            # Checking and creating the traing folder if it not exists
            if not os.path.exists(data_path+'/train/'+word):
                os.makedirs(data_path+'/train/'+word)
            
            # Defining path of the source image
            srcimage = srcdir+"/"+imagefile
            # Defining path of the destination folder
            dstdir=data_path+'/train/'+word
            # Copying
            shutil.copy(srcimage, dstdir)

        else:
            # Checking and creating the testing folder if it not exists
            if not os.path.exists(data_path+'/test/'+word):
                os.makedirs(data_path+'/test/'+word)
            
            # Defining path of the source image
            srcimage = srcdir+"/"+imagefile
            # Defining path of the destination folder
            dstdir=data_path+'/test/'+word
            # Copying
            shutil.copy(srcimage, dstdir)

        traincount +=1



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 10:52:25 2021

@author: Mathew
"""

import os
from shutil import copyfile



  

inputpath = '/Volumes/My Passport/ONI/'
outputpath = '/Users/Mathew/Documents/Current analysis/Analysis/'


for dirpath, dirnames, filenames in os.walk(inputpath):
    structure = os.path.join(outputpath, dirpath[len(inputpath):])
    if not os.path.isdir(structure):
        os.mkdir(structure)
    else:
        print("Folder does already exits!")
        

file_to_copy=[]

file_to_copy.append('Lengths.pdf')
# file_to_copy.append('Area.pdf')
# file_to_copy.append('GDSCSMLM_SR_width_python_clustered.tif')
# file_to_copy.append('Green_flat.tif')

# file_to_copy.append('TOM20-AF647_dSTORM_ThunderSTORM_Render.tif')
for file in file_to_copy:
    
    for root, dirs, files in os.walk(inputpath):
        for name in files:
                if file in name:
                    src=root+'/'+file
                    dst=src.replace(inputpath,outputpath)
                    print(src)
                    print(dst)
                    copyfile(src,dst)


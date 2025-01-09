#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 12:54:33 2025

@author: amartinez
"""

import astropy.io.fits as fits
import numpy as np
import os
import sys
from astropy.table import Table
from astropy.wcs.utils import fit_wcs_from_points
from astropy.wcs import WCS
from astropy.io import fits
import astroalign as aa
from astropy.coordinates import SkyCoord
import astropy.units as u
import matplotlib.pyplot as plt
from astropy.wcs.utils import fit_wcs_from_points
import shutil
import gzip
import subprocess

# %%

field = 20


folder = '/home/data/raw/GNS_2/H/Field/%s/'%(field)
cubes_aligned = '/home/data/alvaro/gns_test/F%s/cubes_aligned/'%(field)
pruebas = '/home/data/alvaro/gns_test/F%s/pruebas/'%(field)
sf_folder = '/home/data/GNS/2021/H/%s/data/'%(field)
clean = '/home/data/GNS/2021/H/%s/cleaned/'%(field)
VVV_fol = '/home/data/VVV/'
ims = '/home/data/GNS/2021/H/20/ims/'


ch_range = [1,2]
#MISSFITS
for chip in range(ch_range[0],ch_range[1]):
    command = ['missfits', cubes_aligned + '%s_image_c%s'%(field,chip), '-c', 'conf.missfits']
    
    try:
        # Run the command
        
        result = subprocess.run(command, check=True)
        # Print standard output and error
        print("Command Output:")
        print(result.stdout)
        print("Command Error (if any):")
        print(result.stderr)
    
    except subprocess.CalledProcessError as e:
        # Handle errors
        print(f"Error: {e}")
        print(f"Standard Output: {e.stdout}")
        print(f"Standard Error: {e.stderr}")
    

for chip in range(3,5):
    command = ['missfits', cubes_aligned + '%s_mask_c%s'%(field,chip), '-c', 'conf.missfits']
    
    try:
        # Run the command
        
        result = subprocess.run(command, check=True)
        # Print standard output and error
        print("Command Output:")
        print(result.stdout)
        print("Command Error (if any):")
        print(result.stderr)
    
    except subprocess.CalledProcessError as e:
        # Handle errors
        print(f"Error: {e}")
        print(f"Standard Output: {e.stdout}")
        print(f"Standard Error: {e.stderr}")
# %%           
sex_folder = '/home/data/alvaro/gns_test/F%s/sextractor/'%(field)
scamp_folder = '/home/data/alvaro/gns_test/F%s/scamp/'%(field)
SWarp_folder = '/home/data/alvaro/gns_test/F%s/SWarp/'%(field)
# %%
#SOURCE-EXTRACTOR
for chip in range(ch_range[0],ch_range[1]):
    command = ['source-extractor', cubes_aligned + '%s_image_c%s.fits'%(field,chip), 
               '-c', 'default_c%s.sex'%(chip)]
    
    try:
        # Run the command
        
        # result = subprocess.run(command, cwd=f'{sex_folder}chip{chip}/',check=True, text=True, capture_output=True)
        result = subprocess.run(command, cwd=f'{sex_folder}chip{chip}/',check=True)
        
        # Print standard output and error
        print("Command Output:")
        print(result.stdout)
        print("Command Error (if any):")
        print(result.stderr)
    
    except subprocess.CalledProcessError as e:
        # Handle errors
        print(f"Error: {e}")
        print(f"Standard Output: {e.stdout}")
        print(f"Standard Error: {e.stderr}")
# %%
#SCAMP
for chip in range(ch_range[0],ch_range[1]):
    command = ['scamp', sex_folder + 'chip%s/%s_image_c%s.cat'%(chip, field,chip), 
                '-c', 'scamp_c%s.conf'%(chip)]
    
    try:
        # Run the command
        
        result = subprocess.run(command, cwd=f'{scamp_folder}chip{chip}/',check=True)
        # Print standard output and error
        print("Command Output:")
        print(result.stdout)
        print("Command Error (if any):")
        print(result.stderr)
    
    except subprocess.CalledProcessError as e:
        # Handle errors
        print(f"Error: {e}")
        print(f"Standard Output: {e.stdout}")
        print(f"Standard Error: {e.stderr}")


#%%
#SWARP
for chip in range(ch_range[0],ch_range[1]):
    
    command = ['SWarp', cubes_aligned+ '%s_image_c%s.fits' %(field, chip), 
               '-c', 'default_c%s.swarp'%(chip), '-HEADER_NAME',scamp_folder + 'chip%s/%s_image_c%s.head'%(chip,field, chip),
               '-WEIGHT_IMAGE',cubes_aligned + '%s_mask_c%s.fits'%(field, chip)]
    
    try:
        # Run the command
        
        result = subprocess.run(command, cwd=f'{SWarp_folder}chip{chip}/',check=True)
        # Print standard output and error
        print("Command Output:")
        print(result.stdout)
        print("Command Error (if any):")
        print(result.stderr)
    
    except subprocess.CalledProcessError as e:
        # Handle errors
        print(f"Error: {e}")
        print(f"Standard Output: {e.stdout}")
        print(f"Standard Error: {e.stderr}")

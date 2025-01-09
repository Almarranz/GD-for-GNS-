#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:38:03 2024

@author: alvaro
"""
from astropy.io import fits
import os

field = 20
cubes_aligned = f'/home/data/alvaro/gns_gd/gns2/F{field}/cubes_aligned/'
bad_folder = f'/home/data/alvaro/gns_gd/gns2/bad_slices/F{field}/'

# Ensure the bad_folder exists
os.makedirs(bad_folder, exist_ok=True)

# Iterate over the chips
for chip in range(1, 5):
    fits_file = cubes_aligned + f"{field}_image_c{chip}.fits"
    extensions_to_remove = [42,	47,	82,	222,	223,	241,	277,	386,	387]

    # Sort extensions in descending order for safe removal
    extensions_to_remove.sort(reverse=True)

    # Open the FITS file
    with fits.open(fits_file, mode='update') as hdulist:
        for ext in extensions_to_remove:
            # Create a new FITS file for the bad slice
            bad_slice_path = os.path.join(bad_folder, f"bad_slice_{chip}_ext{ext}.fits")
            hdu = hdulist[ext]

            # Save the bad slice to the bad folder
            hdu.writeto(bad_slice_path, overwrite=True)

            # Remove the extension from the original FITS file
            del hdulist[ext]

        # Save changes to the FITS file
        hdulist.flush()

    print(f"Processed chip {chip}, removed extensions: {extensions_to_remove}")

# from astropy.io import fits
# %%

field = 20
cubes_aligned = '/home/data/alvaro/gns_gd/gns2/F%s/cubes_aligned/'%(field)
bad_folder = '/home/data/alvaro/gns_gd/gns2/bad_slices/F%s/'%(field)

# Path to your FITS file
for chip in range (1,5):
    # fits_file = cubes_aligned + "70_pointings_f20_c%s.fits"%(chip)
    fits_file = cubes_aligned + "%s_mask_c%s.fits"%(field,chip)
    
    # List of extensions to remove
    # extensions_to_remove = [82, 386, 387]
    
    # Sort extensions in descending order for safe removal
    extensions_to_remove.sort(reverse=True)
    
    # Open the FITS file
    with fits.open(fits_file, mode='update') as hdulist:
        
        # Loop over the extensions to remove them
        for ext in extensions_to_remove:
            del hdulist[ext]  # Remove the extension by its index
        
        # Save changes to the same file
        hdulist.flush()  # Ensure changes are saved to disk
    print(chip)

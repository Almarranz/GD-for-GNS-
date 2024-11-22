#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:38:03 2024

@author: alvaro
"""

from astropy.io import fits


field = 20
cubes_aligned = '/home/data/alvaro/gns_test/F%s/cubes_aligned/'%(field)

# Path to your FITS file
for chip in range (1,5):
    # fits_file = cubes_aligned + "70_pointings_f20_c%s.fits"%(chip)
    fits_file = cubes_aligned + "MASK_70_pointings_f20_c%s.fits"%(chip)
    
    # List of extensions to remove
    extensions_to_remove = [82, 386, 387]
    
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

# BMP-2-DataPecker
Python script to convert 640x200 monochrome bitmaps into loadable files that can be displayed on the Data Becker Hi-Res graphics card and my *DataPecker* clone card for the CBM PET 8032 series.

# The Background
The Data Becker Hi-Res graphics card can display monochrome (green on black) images with a resolution of 640x200 pixels. The image Data is Stored in Blocks of 8 bytes representing 8x8 pixel blocks. BMP files store the lines linearly in a bottom-first order. This script reads the BMP header, checks that the image has the correct dimensions, and rearranges the image lines to create a file for the CBM PET. This file can be loaded directly into the screen memory of the Data Becker Hi-Res using the cards !recall basic extension command.

# The Usage
* Create a suitable 620x200x1Bit BMP file (e.g.: Windows Paint: Select *save as: bmp* and set the file type to *monochrome bmp*.
* Run the script: bmp2datapecker.py sourcefile destinationfile
* Transfer the destinationfile to your PET equipped with a Data Becker Hi-Res card and simply load the file using the !recall command provided by the cards basic extension.

# The License
This work is licensed under a Creative Commons Zero v1.0 Universal License.

See https://creativecommons.org/publicdomain/zero/1.0/.

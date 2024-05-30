"""bmp2datapecker.py: Python script to convert 640x200 monochrome bitmaps
into loadable files that can be displayed on the Data Becker Hi-Res graphics card
and my *DataPecker* clone card for the CBM PET 8032 series."""

__author__      = "InsaneDruid"
__copyright__   = "Copyright 2024"
__license__     = "Creative Commons Zero v1.0 Universal"

class wrongwidth(Exception):
    pass
class wrongheight(Exception):
    pass

import argparse
parser = argparse.ArgumentParser(description="BMP to PET")
parser.add_argument("sourcefile", help="the name of the bmp file.")
parser.add_argument("destinationfile", help="the name of the file to be created.")
parser.add_argument("-i","--invert",action="store_true", help="write inverted image data")
args = parser.parse_args()
backpadding = 16008
fill = 0


print(f"reading file {args.sourcefile}")

with open(args.sourcefile, "rb") as file:
    
    # read pixeldata start offset
    file.seek(10) 
    pixeldata = int.from_bytes(file.read(4), byteorder='little')
    
    # read file width
    file.seek(18)
    width = int.from_bytes(file.read(4), byteorder='little') 
    
    # read file height
    file.seek(22)
    height = int.from_bytes(file.read(4), byteorder='little') 

    try:
        if width != 640:
            raise wrongwidth(width)
        if height != 200:
            raise wrongheight(height)
        
    except wrongwidth:
        print(f"{args.sourcefile} has width of {width}. Must be 640")
        quit()
    
    except wrongheight:
        print(f"{args.sourcefile} has width of {height}. Must be 200")
        quit()

    padding = width % 4
    currentline = height
    
    if args.invert==True:
        print ("image will be inverted")
    print(f"writing file {args.destinationfile}")
    count = 0
    with open(args.destinationfile,"wb") as writefile:
    
        # seek to first image data position
        file.seek(pixeldata)                           
        while currentline >0:
            content = file.read((width+padding) // 8)               # reading one full line of the image, last to first

            textline = (currentline - 1) // 8                       # line is in which of the 25 charlines
            charline = (currentline - 1) % 8                        # line is in which of the 8 lines per charline

            for i in range(80):
                seek = 8 + (textline * 640) + (charline) + (i * 8)  # 8Byte leadin-Padding + line position + 8 byte interleave
                writefile.seek(seek)

                # invert the image data?
                if args.invert==True:                       
                    writefile.write((255-content[i]).to_bytes(1))        
                else:
                    writefile.write(content[i].to_bytes(1))
            
            currentline = currentline -1

        #writing trailing fillbytes
        writefile.seek(backpadding)
        for i in range (376):
            writefile.write(fill.to_bytes(1))

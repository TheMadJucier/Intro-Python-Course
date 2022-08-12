#
# ps8pr3.py (Problem Set 8, Problem 3)
#
# Image processing with loops and image objects
#
# Computer Science 111
# 
# File: ps8pr3.py
# Author: Wadner Simon, 7/31/2022
# Description: Image processing with loops and image objects

from cs111png import *

#Function 1
def invert(filename):
    """ loads a PNG image from the file with the specified filename
        and creates a new image in which the colors of the pixels are
        inverted.
        input: filename is a string specifying the name of the PNG file
               that the function should process.
        No value is returned, but the new image is stored in a file
        whose name is invert_filename, where filename is the name of
        the original file.
    """
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()

    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            # get the RGB values of the pixel at row r, column c
            rgb = img.get_pixel(r, c)
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]

            # invert the colors of the pixel at row r, column c
            new_rgb = [255 - red, 255 - green, 255 - blue]
            img.set_pixel(r, c, new_rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'invert_' + filename
    img.save(new_filename)

#Function 2
def brightness(rgb):
    """ takes the RGB values of a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    return (21*red + 72*green + 7*blue) // 100

### PUT YOUR WORK FOR PROBLEM 4 BELOW. ###

#Function 3
def grayscale(filename):
    
    img = load_image(filename)
    
    height = img.get_height()
    width = img.get_width()
    
    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            # get the RGB values of the pixel at row r, column c
            rgb = img.get_pixel(r, c)
           

            greyscale_img = brightness(rgb)
            rgb[0] = greyscale_img
            rgb[1] = greyscale_img
            rgb[2] = greyscale_img
            
            img.set_pixel(r,c, rgb)
            
    new_filename = 'gray_' + filename
    img.save(new_filename)
    
    
#Function 4
def bw(filename,threshold):
    
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()

    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            # get the RGB values of the pixel at row r, column c
            rgb = img.get_pixel(r, c)
            
            bw_test = brightness(rgb)
            
            if threshold < bw_test:
                img.set_pixel(r,c, [255,255,255])
            else:
                img.set_pixel(r,c, [0,0,0])
    new_filename = 'bw_' + filename
    img.save(new_filename)


#Function 5
def fold_diag(filename):
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()

    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            # get the RGB values of the pixel at row r, column c
            rgb = img.get_pixel(r, c)
            
            if c >= r :
                img.set_pixel(r,c, rgb)
            else:
                img.set_pixel(r,c,[255,255,255])
                
    new_filename = 'fold_' + filename
    img.save(new_filename)
                
    
    
                
    

    
    

#
# ps8pr4.py (Problem Set 8, Problem 4)
#
# Image processing with loops and image objects
#
# Computer Science 111
#
# File: ps8pr4.py
# Author: Wadner Simon, 7/31/2022
# Description: Image processing with loops and image objects

from cs111png import *


#Function 1
def flip_vert(filename):
    """that loads the PNG image file with the specified filename and 
        creates a new image in which the original image is “flipped” 
        vertically.
    """
    
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()
    
    img = load_image(filename)
    height = img.get_height()
    width = img.get_width()
    new_img = Image(height, width)   # create a new, blank image object
            
    
            
    for r in range(height): #row
        for c in range(width): #column
            
            rgb = img.get_pixel(height-r-1,c) #flipping
        
            new_img.set_pixel(r,c,rgb) #flipped image is being set
            


        
    new_filename = 'flipv_' + filename
    new_img.save(new_filename) 


#function 2
def mirror_vert(filename):
    """that loads the PNG image file with the specified filename and creates 
        a new image in which the original image is “mirrored” vertically
    """
    
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()
    
    img = load_image(filename)
    height = img.get_height()
    width = img.get_width()
    new_img = Image(height, width)   # create a new, blank image object
            
    
    for r in range(height): #row
        for c in range(width): #column
            if r < height//2: 
                rgb = img.get_pixel(r,c)
                new_img.set_pixel(r,c,rgb)
            else:
                rgb = img.get_pixel(height-r-1,c)
                new_img.set_pixel(r,c,rgb)
                


        
    new_filename = 'mirrorv_' + filename
    new_img.save(new_filename)
            
    
    

    
#Function 3
def reduce(filename):
    """that loads the PNG image file with the specified filename and creates 
       a new image that is half the size of the original image
    """
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()
    
    img = load_image(filename)
    height = img.get_height()
    width = img.get_width()
    r_height = height//2
    r_width = width//2
    new_img = Image(r_height, r_width)   # create a new, blank image object
            
    
            
    for r in range(r_height): #row
        for c in range(r_width): #column
            
            rgb = img.get_pixel(r*2,c*2) #reducing by multi by 2
            new_img.set_pixel(r,c,rgb)
         
    new_filename = 'reduce_' + filename
    new_img.save(new_filename)
    
  
#Function 4
def extract(filename, rmin, rmax, cmin, cmax):
    """extract(filename, rmin, rmax, cmin, cmax) that loads the PNG image 
        file with the specified filename and extracts a portion of the original
        image that is specified by the other four parameters.
    """
     
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()
    
    img = load_image(filename)
    height = img.get_height()
    h_new = rmax - rmin 
    w_new = cmax - cmin
    width = img.get_width()
    new_img = Image(h_new,w_new)   # create a new, blank image object with 
                                   # different dimensions
    
    for r in range(h_new): #row
        for c in range(w_new): #column
        
            rgb = img.get_pixel(rmin+r,cmin+c)
            new_img.set_pixel(r,c,rgb)
            
                
        

    new_filename = 'extract_' + filename
    new_img.save(new_filename)
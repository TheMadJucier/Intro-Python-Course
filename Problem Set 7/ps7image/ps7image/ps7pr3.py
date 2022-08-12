#
# ps7pr3.py (Problem Set 7, Problem 3)
#
# Images as 2-D lists
#
# Computer Science 111
# 
 
from hmcpng import *

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []
    
    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels



#Function 1
def blank_image(height, width):
    """creates and returns a 2-D list of pixels
        with height rows and width columns in which 
        all of the pixels are green (i.e., have RGB 
        values [0,255,0])
    """
    
    image = create_uniform_image(height, width, [0,255,0]) #getting blank img
            
    return image 


#Function 2
def flip_horiz(pixels):
    """takes the 2-D list pixels containing pixels for
        an image, and that creates and returns a new 2-D 
        list of pixels for an image in which the original 
        image is “flipped” horizontally.
    """
    
    flip = blank_image((len(pixels)),(len(pixels[0])))

    for r in range(len(pixels)): #row
        for c in range(len(pixels[0])): #column
            flip[r][c] = pixels[r][-c-1] #c being taken backwards
   
    return flip


#Function 3
def flip_vert(pixels):
    """takes the 2-D list pixels containing pixels for
        an image, and that creates and returns a new 2-D 
        list of pixels for an image in which the original 
        image is “flipped” vertically.
    """
    
    flip = blank_image(len(pixels),len(pixels[0])) #getting blank img
    
        
    for r in range(len(pixels)): #row
        for c in range(len(pixels[0])):#column
            flip[r][c] = pixels[-r-1][c] #r being taken backwards
            
    
  
    return flip



#Function 4
def transpose(pixels):
    """takes the 2-D list pixels containing pixels for an image, 
       and that creates and returns a new 2-D list that is the 
       transpose of pixels
    """
    
    transpose = blank_image(len(pixels[0]),len(pixels)) #switching row & col

    for r in range(len(transpose)): #row
        for c in range(len(transpose[0])): #col
            transpose[r][c] = pixels[c][r] # rc = cr
            
    return transpose


#Function 5
def rotate_clockwise(pixels):
    """hould rotate the original image clockwise by 90 degrees.
    """
    
    ro_clock = transpose(pixels) #transposing pixels

    for r in range(len(ro_clock)): #row
        for c in range(len(ro_clock[0])): #column
            ro_clock[r][c] = pixels[-c-1][r] #r being taken backwards
  
    return ro_clock


#Function 6
def rotate_counterclockwise(pixels):
    """should rotate the original image counterclockwise by 90 degrees
    """
    
    ro_count = transpose(pixels) #transposing pixels first

    for r in range(len(ro_count)):
        for c in range(len(ro_count[0])):
            ro_count[r][c] = pixels[c][-r-1] #r being taken backwards
  
    return ro_count

    

#pixels = load_pixels('spam.png')
#flipped = flip_horiz(pixels)
#save_pixels(flipped, 'horiz3_spam.png')  



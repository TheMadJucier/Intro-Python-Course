#
# ps7pr2.py (Problem Set 7, Problem 2)
#
# Matrix operations
#
# Computer Science 111
# 

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Enter a new matrix')
    print('(1) Negate the matrix')
    print('(2) Multiply a row by a constant')
    print('(3) Add one row to another')
    print('(4) Add a multiple of one row to another')
    print('(5) Transpose the matrix')
    print('(6) Quit')
    print()

def print_matrix(matrix):
    """ prints the specified matrix in rectangular form.
        input: matrix is a 2-D list numbers
    """
    ## You will revise this function. 
    
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            
            matrix[r][c] = matrix[r][c] # setting matrix
            print('%7.2f' % matrix[r][c], end=' ')
            
        print()
    

       
def get_matrix():
    """ gets a new matrix from the user and returns it
    """
    matrix = eval(input('Enter a new 2-D list of numbers: '))
    return matrix



def negate_matrix(matrix):
    """ negates all of the elements in the specified matrix
        inputs: matrix is a rectangular 2-D list of numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix[r][c] *= -1
    # We don't need to return the matrix!
    # All changes to the matrix will still be there when the
    # function returns, because we received a copy of the
    # *reference* to the matrix used by main().

#Add your functions for options 2-5 here. ###


#Function 2
def mult_row(matrix, r, m):
    """that multiplies row r of the specified matrix by 
        the specified multiplier m.
    """
    row = r
    
    for r in range(len(matrix)): #row 
        for c in range(len(matrix[0])): #column
        
            if r == row: #checking the row = r
                matrix[r][c] *= m
                
            else: # not row r
                matrix[r][c] = matrix[r][c]
                
 
#Function 3
def add_row_into(matrix, rs, rd):
    """add_row_into(matrix, rs, rd) that takes the specified 
        2-D list matrix and adds each element of row rs 
        (the source row) to the corresponding element of row 
        rd (the destination row).
    """
    #row_s = rs
    #row_d = rd
    
    for r in range(len(matrix)): #row
        for c in range(len(matrix[0])): #column
            
            if r == rd: #finding destination
                matrix[rd][c] += matrix[rs][c]
                
            else:
 
                matrix[r][c] = matrix[r][c]


#Function 4                
def add_mult_row_into(matrix, m, rs, rd):
    """add_row_into(matrix, rs, rd) that takes the specified 
        2-D list matrix and adds each element of row rs 
        (the source row) to the corresponding element of row 
        rd (the destination row).
    """

    
    for r in range(len(matrix)): #row
        for c in range(len(matrix[0])): #column
        
            if r == rd: # finding destination
                matrix[rd][c] += matrix[rs][c] * m #adding rs to rd times m
                
            else: # not destination
                matrix[r][c] = matrix[r][c] 

#Function 5
def transpose(matrix):
    """The transpose of an n x m matrix is a new m x n matrix in 
        which the rows of the original matrix become the columns 
        of the new one, and vice versa.
    """
    t_matrix = [] #intializing
    
    for r in range(len(matrix[0])): # new matrix
        row = [0] * len(matrix)   
        t_matrix += [row]
        
    for r in range(len(matrix[0])): #row
        for c in range(len(matrix)): #column
        
            t_matrix[r][c] = matrix[c][r] #rc = cr
            
    return t_matrix
    
    


def main():
    """ the main user-interaction loop
    """
    ## The default starting matrix.
    ## DO NOT CHANGE THESE LINES.
    matrix = [[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12]]

    while True:
        
        print_matrix(matrix)
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 0:
            matrix = get_matrix()
            display_menu()
            choice = int(input('Enter your choice: '))
            
        
        elif choice == 1:
            negate_matrix(matrix)
            display_menu()
            choice = int(input('Enter your choice: '))
            

        ## add code to handle the other options here
        elif choice == 2:
            row = int(input("Index of Row: "))
            mult = float(input("Multiplier: "))
            mult_row(matrix,row, mult)
            display_menu()
            choice = int(input('Enter your choice: '))
                      
        elif choice == 3:
            rs = int(input("Source of Matrix: "))
            rd = int(input("Destination of Matrix: "))
            add_row_into(matrix, rs, rd)
            display_menu()
            choice = int(input('Enter your choice: '))
            
            
        elif choice == 4:
            rs = int(input("Source of Matrix: "))
            rd = int(input("Destination of Matrix: "))
            mult = float(input("Multiplier: "))
            add_mult_row_into(matrix, rs, rd)
            display_menu()
            choice = int(input('Enter your choice: '))
            
        
        elif choice == 5:
            transpose(matrix)
            display_menu()
            choice = int(input('Enter your choice: '))
            

        elif choice == 6:
            break
        else:
            print('Invalid choice. Try again.')

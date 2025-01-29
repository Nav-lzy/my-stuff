import random
import time
import math

# Program to practice matrix multiplication, because
# otherwise I will never learn this shit fully

##########################################################
# Matrix representation:                                 #
# test_matrix = [[1, 2, 3],                              #
#                [4, 5, 6],                              #
#                [7, 8, 9]]                              #
#                                                        #
# test_matrix[i][j] selects the i-th row and j-th column #
#                                                        #
##########################################################


def rand_elem(l: list):
    '''
    Returns random element of a list
    '''
    return l[random.randint(0, len(l) - 1)]

def init_rand_matrix(dim_rows: int, dim_col: int, rand_min = 0, rand_max = 9) -> list[list[int]]:
    '''
    Returns dim_rows x dim_col matrix with random initialized values from range rand_min to rand_max
    '''
    # check for valid rand_min and rand_max:
    if rand_min > rand_max:
        print(f"rand_min = {rand_min} is bigger than rand_max = {rand_max}")
        print("Using default parameter rand_min = 0 and rand_max = 9\n")
        return init_rand_matrix(dim_rows, dim_col)

    mat = []
    for i in range(dim_rows):
        # Add new row
        mat.append([])
        for j in range(dim_col):
            # Fill in random value in i-th row and j-th column
            mat[i].append(random.randint(rand_min, rand_max))
    return mat

def print_pretty_matrix(mat: list[list]):
    '''
    Prints a pretty matrix
    '''
    # Get matrix dimensions
    d = len(mat)
    n = len(mat[0])

    # Determine the maximum width of any number in the matrix
    max_width = max(len(str(num)) for row in mat for num in row)
    lines = "--" + (n * max_width * "-") + ((n - 1) * "--") + "--\n"

    pretty_matrix = ""
    pretty_matrix += lines
    for i in range(d):
        # Start every row with "| "
        pretty_matrix += "| "
        for j in range(n):
            if j == (n - 1):  # Not print the last space
                pretty_matrix += f"{mat[i][j]:>{max_width}}"   # Rigth-aligns the values
            else:
                pretty_matrix += f"{mat[i][j]:>{max_width}}  " # Rigth-aligns the values
        # End every row with " |\n"
        pretty_matrix += " |\n"
    pretty_matrix += lines
    print(pretty_matrix)

def print_pretty_matrix_mult(mat1: list[list], mat2: list[list]):
    '''
    Prints a pretty matrix multiplication
    '''
    # Get matrix dimensions
    d1, n1 = len(mat1), len(mat1[0])
    d2, n2 = len(mat2), len(mat2[0])
    
    d_max = max(d1, d2)
    d_min = min(d1, d2)

    # Compute number of lines to push down smaller matrix (for pretty aligment purposes)
    # Do not ask how I came up with this formula. It just works. More detailed notes in
    # Goodnotes document
    push_down_factor = math.ceil((d_max - d_min) / 2)

    # Determine the maximum width of all number in the matrix
    max_width1 = max(len(str(num)) for row in mat1 for num in row)
    max_width2 = max(len(str(num)) for row in mat2 for num in row)

    spaces1 = "  " + (n1 * max_width1 * " ") + ((n1 - 1) * "  ") + "  "
    spaces2 = "  " + (n2 * max_width2 * " ") + ((n2 - 1) * "  ") + "  "
    line1   = "--" + (n1 * max_width1 * "-") + ((n1 - 1) * "--") + "--"
    line2   = "--" + (n2 * max_width2 * "-") + ((n2 - 1) * "--") + "--"
    
    if d1 >= d2: # Align mat2 to mat1 because mat1 has bigger or equal row size
        line = line1 + "\n"
        pretty_matrix_mult = ""
        pretty_matrix_mult += line
        for i in range(max(d1, d2)):
            pretty_matrix_mult += "| " # Start every row with "| "
            inside_print_region = (push_down_factor <= i and i < push_down_factor + d_min)
            inside_line_region  = (i == push_down_factor - 1 or i == push_down_factor + d_min)
            for j in range(n1 + n2):
                if j < n1: # Still values of mat1
                    if j == n1 - 1:
                        pretty_matrix_mult += f"{mat1[i][j]:>{max_width1}}"   # Print no space after last number
                    else: 
                        pretty_matrix_mult += f"{mat1[i][j]:>{max_width1}}  " # Print space after every number except last one

                elif not inside_print_region and j >= n1:
                    # pretty_matrix_mult += " |   | " + (max_width2 * n2) * " " + (n2 - 1) * "  " + " |\n"
                    continue # Stop current iteration
                
                else: # Switch to values of mat2    
                    if j == n1: # Reached end of first matrix; Add space between them
                        pretty_matrix_mult += " |   | "
                    if j - n1 == n2 - 1:
                        pretty_matrix_mult += f"{mat2[i - push_down_factor][j - n1]:>{max_width1}}"   # Print no space after last number
                    else:
                        pretty_matrix_mult += f"{mat2[i - push_down_factor][j - n1]:>{max_width2}}  " # Print space after every number except last one
            # End every row with " |\n"
            pretty_matrix_mult += " |\n"

        pretty_matrix_mult += line

    else: # Align mat1 to mat2 because mat2 has bigger row size
        line = spaces1 + "   " + line2 + "\n"

        pretty_matrix_mult = ""
        pretty_matrix_mult += line
        for i in range(max(d1, d2)):

            # print(pretty_matrix_mult)
            # print("next:")

            inside_print_region = (push_down_factor <= i and i < push_down_factor + d_min)
            inside_line_region = i == push_down_factor - 1 or i == push_down_factor + d_min

            if inside_line_region:
                pretty_matrix_mult += "--"  # print line on top or on bottom of mat1 (start or end of mat1)
            elif inside_print_region:
                pretty_matrix_mult += "| "  # print "| " at start of line  (inside mat1)
            else:                           
                pretty_matrix_mult += "  "  # print empty space (outside of mat1) 

            for j in range(n1 + n2):
                if j < n1 and inside_print_region: # Still in mat1 and inside print region
                    if j == n1 - 1: # Not print the last space
                        pretty_matrix_mult += f"{mat1[i - push_down_factor][j]:>{max_width1}}"   # Print no space after last number
                    else: 
                        pretty_matrix_mult += f"{mat1[i - push_down_factor][j]:>{max_width1}}  " # Print space after every number except last one

                elif j < n1 and not inside_print_region: # Still in mat1 but outside print region
                    puffer = " "
                    if inside_line_region:
                        puffer = "-"

                    if j == n1 - 1: # Not print the last space
                        pretty_matrix_mult += max_width1 * puffer # Adds puffer
                    else: 
                        pretty_matrix_mult += max_width1 * puffer + 2 * puffer # Adds puffer
                
                # Switch to values of mat2
                else:
                    if j == n1: # Reached end of first matrix; Add space between them
                        if inside_print_region: 
                            pretty_matrix_mult += " |   | "
                        elif inside_line_region:
                            pretty_matrix_mult += "--   | "
                        else:
                            pretty_matrix_mult += "     | "


                    if j - n1 == n2 - 1: # Not print the last space
                        pretty_matrix_mult += f"{mat2[i][j - n1]:>{max_width2}}"   # Print no space after last number
                    else:
                        pretty_matrix_mult += f"{mat2[i][j - n1]:>{max_width2}}  " # Print space after every number except last one

            # End every row with " |\n"
            pretty_matrix_mult += " |\n"

        pretty_matrix_mult += line
    print(pretty_matrix_mult)

def matrix_multiplication(mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
    # Get matrix dimensions
    d = len(mat1)    # Rows of mat1
    n = len(mat2)    # Columns of mat1; Rows of mat2
    m = len(mat2[0]) # Columns of mat2

    # Initialise result matrix
    res_mat = []
    for i in range(d):
        # Add new row
        res_mat.append([])
        for j in range(m):
            res_val = 0
            for k in range(n):
                res_val += mat1[i][k] * mat2[k][j]
            
            res_mat[i].append(res_val)

    return res_mat

# ----------------------------------------------------------------------
# Program starts here

max_dim = 4
dimensions = list(range(1, max_dim + 1))

# Compute fitting dimensions
d = rand_elem(dimensions) # Rows of mat1
n = rand_elem(dimensions) # Columns of mat1; Rows of mat2
m = rand_elem(dimensions) # Columns of mat2
# d = 2
# n = 2
# m = 3

# Initialise Matrices with random values
mat1, mat2 = init_rand_matrix(d, n), init_rand_matrix(n, m)

# Multiply mat1 and mat2
res = matrix_multiplication(mat1, mat2)

# Print the results
print(f"M ({d} x {n} - Matrix):")
print_pretty_matrix(mat1)

print(f"N ({n} x {m} - Matrix):")
print_pretty_matrix(mat2)

print_pretty_matrix_mult(mat1, mat2)

input("Press enter to start the timer\n")

# Record the start time
start_time = time.time()

input("Press enter to see N and M multiplied\n")

# Calculate the elapsed time
elapsed_time = time.time() - start_time

# Convert the elapsed time to minutes and seconds
minutes = int(elapsed_time // 60)
seconds = int(elapsed_time % 60)

print(f"M * N ({d} x {m} - Matrix):")
print_pretty_matrix(res)

# Output the elapsed time in a human-readable format
print(f"Time taken: {minutes} minutes and {seconds} seconds")

# give input options for user to give their calculation result
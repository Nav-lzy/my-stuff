import random
import time

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
            # Rigth-aligns the values and
            if j == (n - 1):  # Not print the last space
                pretty_matrix += f"{mat[i][j]:>{max_width}}"
            else:
                pretty_matrix += f"{mat[i][j]:>{max_width}}  "
        # End every row with " |\n"
        pretty_matrix += " |\n"
    pretty_matrix += lines
    print(pretty_matrix)

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

max_dim = 5
dimensions = list(range(1, max_dim + 1))

# Compute fitting dimensions
d = rand_elem(dimensions) # Rows of mat1
n = rand_elem(dimensions) # Columns of mat1; Rows of mat2
m = rand_elem(dimensions) # Columns of mat2

# Initialise Matrices with random values
mat1, mat2 = init_rand_matrix(d, n), init_rand_matrix(n, m)

# Multiply mat1 and mat2
res = matrix_multiplication(mat1, mat2)

# Print the results
print(f"M ({d} x {n} - Matrix):")
print_pretty_matrix(mat1)

print(f"N ({n} x {m} - Matrix):")
print_pretty_matrix(mat2)

# Record the start time
start_time = time.time()

input("Press enter to see the matrices multiplied \n")

# Calculate the elapsed time
elapsed_time = time.time() - start_time

# Convert the elapsed time to minutes and seconds
minutes = int(elapsed_time // 60)
seconds = int(elapsed_time % 60)

print(f"M * N ({d} x {m} - Matrix):")
print_pretty_matrix(res)

# Output the elapsed time in a human-readable format
print(f"Time taken: {minutes} minutes and {seconds} seconds")

# give input options for user to give their calcution result

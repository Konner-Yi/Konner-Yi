import random

#IMPORTANT: NUMBER OF STARS IS THE NUMBER OF MULTIPLICATIONS DIVIDED BY 100000
#BEST GUESS FOR BIG O: O(sqrt(x))
def matrix_multiply(m1, m2, n):
    result = []
    counter = 0
    for r in range(n):
        new_row = []
        for c in range(n):
            new_row.append(0)
            for i in range(n):
                new_row[c] += m1[r][i] * m2[i][c] #Here!
                counter+=1
        result.append(new_row)
    return counter

def generate_n_by_n_matrix(n):
    result = []
    for r in range(n):
        row = []
        for c in range(n):
            row.append(r * n + c)
        result.append(row)
    return result

for n in range(20, 201, 20):
    matrix1 = generate_n_by_n_matrix(n)            # generate an nxn matrix (matrix1)
    matrix2 = generate_n_by_n_matrix(n)            # generate an nxn matrix (matrix2)
    number = matrix_multiply(matrix1, matrix2, n)  # multiply the two matrices
    print(f"{n} ", end="")
    for x in range(int((number/100000))):
        print('*', end="")
    print("")


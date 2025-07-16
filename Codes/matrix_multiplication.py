'''
Write a Python function that computes the dot product of a matrix and a vector.
 The function should return a list representing the resulting vector
  if the operation is valid, or -1 if the matrix and vector dimensions
  are incompatible. A matrix (a list of lists) can be dotted with a vector
   (a list) only if the number of columns in the matrix equals the
    length of the vector. For example, an n x m matrix requires a vector of length m.

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

for i in range(len(A)):
    for j in  range(len(B[0])):
        for k in range(len(B)):
            result[i][j] +=A[i][k] * B[k][j]

for row in result:
    print(row)

# Vector Multiplied to a Matrix

A=[
    [1, 2, 3],
    [4, 5, 6]
]

v =[7, 8 , 9]

result = [0 for _ in range(len(A))]

for i in range(len(A)):
    for j in range(len(v)):
        result[i]+=A[i][j]*v[j]

print(result)



def get_vector():
    v = input("Enter a vector with spaces:")
    v = [int(x) for x in v.split()]
    print(v)
    return v

#a=get_vector()

def get_matrix(rows, cols):
    matrix =[]
    for i in range(rows):
        row = input(f"Enter row values {i+1} with {cols}:")
        row_list = [int(x) for x in row.split()]
        matrix.append(row_list)

    return matrix
#A=get_matrix()

import numpy as np

def matrix_multi(matrix, vector):
    result = []
    for row in matrix:
        r =0
        for i in range(len(vector)):
            r += row[i]*vector[i]
        result.append(r)


def main():
    rows=int(input("Rows: "))

    cols = int(input("Cols: "))

    matrix = get_matrix(rows, cols)

    vector =(input(f"Enter vector of {cols} numbers: "))

    vector = [int(x) for x in vector.split()]

    result = matrix_multi(matrix, vector)
    print("Results: ", result)

main()

'''
def matrix_dot_vector(rows, cols):
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.

    v = input("Enter a vector with spaces: ")
    v = [int(x) for x in v.split(x)]

    matrix = []

    for i in range(rows):
        row = input(f"enter row values {i + 1} with{cols}")
        row_list = matrix.append([int(x) for x in row.split()])

    result = []
    for row in matrix:
        r = 0
        for i in range(len(vector)):
            r += row[i] * vector[i]
            result.append(r)

    return result

V = matrix_dot_vector(2, 3)
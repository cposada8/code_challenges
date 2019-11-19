# https://www.codewars.com/kata/matrix-determinant/train/python


def print_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        print(matrix[i])


def get_sub_matrix(matrix, i, j):
    # this function returns a submatrix of the original matrix
    # if the len(matrix)==n then the len(submatrix)== n-1.
    # does not contain any element in the row i
    # does not contain any element in the column j

    n = len(matrix)
    submatrix = []
    for row in range(n):
        if row != i:
            actual_row = []
            for col in range(n):
                if col != j:
                    actual_row.append(matrix[row][col])
            submatrix.append(actual_row)
    return submatrix


def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        return a*d-b*c

    matrix_determinant = 0
    sign = 1
    for j in range(n):
        constant = matrix[0][j]
        submatrix = get_sub_matrix(matrix, 0, j)
        matrix_determinant += (-1)**(j)*constant*determinant(submatrix)
    return matrix_determinant


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    matrix1 = [[2, 4, 2], [3, 1, 1], [1, 2, 0]]
    matrix2 = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]
    matrix3 = [[2, 4, -3], [1, 8, 7], [2, 3, 5]]
    matrix4 = [[1, 2, 3, 4], [5, 0, 2, 8], [3, 5, 6, 7], [2, 5, 3, 1]]
    matrix5 = [[2, 5, 3, 6, 3],
               [17, 5, 7, 4, 2],
               [7, 8, 5, 3, 2],
               [9, 4, -6, 8, 3],
               [2, -5, 7, 4, 2]]

    matrix6 = [[6, -7, 9, -2, 9],
               [3, -5, 2, -6, -6],
               [3, 0, -5, -1, -6],
               [9, -4, 9, 8, -3],
               [-9, -3, -10, 2, -9]]

    # print(determinant(matrix6))

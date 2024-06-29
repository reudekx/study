def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def horizontal_flip(matrix):
    return [row[::-1] for row in matrix]

def vertical_flip(matrix):
    return matrix[::-1]

def rotate_90(matrix):
    return horizontal_flip(transpose(matrix))

def rotate_180(matrix):
    return vertical_flip(horizontal_flip(matrix))

def rotate_270(matrix):
    return vertical_flip(transpose(matrix))

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original matrix:")
for row in matrix:
    print(row)

print("\n90-degree rotation:")
for row in rotate_90(matrix):
    print(row)

print("\n180-degree rotation:")
for row in rotate_180(matrix):
    print(row)

print("\n270-degree rotation:")
for row in rotate_270(matrix):
    print(row)
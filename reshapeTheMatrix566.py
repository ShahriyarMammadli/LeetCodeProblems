# Shahriyar Mammadli
# LeetCode problem '521. Longest Uncommon Subsequence I' solution
from functools import reduce

def matrixReshape(mat, r, c):
    if len(mat) * len(mat[0]) != r * c:
        return mat
    flat_list = reduce(lambda x, y: x+y, mat)
    return [flat_list[i:i + c] for i in range(0, len(flat_list), c)]


print(matrixReshape([[1, 2], [3, 4]], 1, 4))


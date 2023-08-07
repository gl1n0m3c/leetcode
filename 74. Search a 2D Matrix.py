# https://leetcode.com/problems/search-a-2d-matrix/submissions/

def bin_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (right + left) // 2
        if array[middle] == target:
            return True
        elif array[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return False

def searchMatrix(matrix, target):
    for row in matrix:
        if row[-1] == target:
            return True
        if row[-1] > target:
            return bin_search(row, target)
    return False
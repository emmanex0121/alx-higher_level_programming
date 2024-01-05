#!/usr/bin/python3

import copy


def matrixDivision(arr): 
	res = [[0]*len(arr[0])]*len(arr)
	#res = [[]]*len(arr)
	#res = copy.copy(arr)
	for i in range(len(res)):
		temp = 0
		for j in range(len(res[i])):
			temp = arr[i][j] // 2
			res[i][j] = temp
			#res[i].insert(j,arr[i][j]//2)
			print("res[",i,"][",j,"]: ",res)
	#print(res)
	return res
	
"""
def matrixDivision(arr):
	return [[j//2 for j in i] for i in arr]
"""

"""
def matrixDivision(arr, div):
    new_mat = [[]] * len(arr)

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            new_mat[i].append(arr[i][j] / div)
    return new_mat
    """
	

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6]]
    print(matrixDivision(matrix))

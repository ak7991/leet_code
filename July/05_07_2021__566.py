from typing import List
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat) * len(mat[0]):
            return mat
        temp_row = []
        new_mat = []
        for row in mat:
            temp_row += row
            while len(temp_row) >= c:
                new_mat.append(temp_row[:c])
                temp_row = temp_row[c:]
        return new_mat

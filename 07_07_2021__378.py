import bisect
import numpy as np
from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        i, j = divmod(k - 1, len(matrix))
        # n = len(matrix)
        refused_elements = (i + j) * (i + j + 1) / 2
        k_left = k - refused_elements
        r, c = i + j, 0
        sorted_diag = []
        while r >= 0:
            element = matrix[r][c]
            idx = bisect.bisect_left(sorted_diag, element)
            sorted_diag.insert(idx, element)
            r -= 1
            c += 1
        return sorted_diag[k_left - 1]
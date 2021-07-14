import bisect
from typing import List

class Solution:
    def prefix_sum(self, row, k):
        ans = float("-inf")
        result_heap = []
        result_heap.append(0)
        running_sum = 0
        for element in row:
            running_sum += element
            delta_needed = running_sum - k
            idx = bisect.bisect_left(result_heap, delta_needed)  # TC logn
            if delta_needed > 0:
                if idx < len(result_heap) and result_heap[idx] == delta_needed:
                    result = running_sum - delta_needed
                elif idx == len(result_heap):
                    result = float("-inf") # not a possible candidate
                else:
                    if running_sum - result_heap[idx] <= k:
                        result = running_sum - result_heap[idx]
                    else:
                        result = float("-inf") # not a possible candidate
            else:
                if idx < len(result_heap) and result_heap[idx] == delta_needed:
                    result = running_sum - delta_needed
                elif idx == len(result_heap):
                    result = running_sum
                else:
                    if running_sum - result_heap[idx] <= k:
                        result = running_sum - result_heap[idx]
                    else:
                        result = running_sum
                
            ans = max(ans, result)  # ans <= k (always) [no check needed]
            result_heap.insert(bisect.bisect_left(result_heap, running_sum), running_sum)
        return ans  # Can be -inf

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = float("-inf")
        i = 0
        while i < m:
            i1 = i
            running_col_cum_sum = [0] * n
            while i1 < m:
                j = 0
                while j < n:
                    running_col_cum_sum[j] += matrix[i1][j]
                    j += 1
                curr_ans = self.prefix_sum(running_col_cum_sum, k)
                ans = max(ans, curr_ans)
                i1 += 1
            i += 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,0,1],[0,-2,3]]
    k = 3
    print("---------->", sol.maxSumSubmatrix(matrix, k))
    matrix = [[2,2,-1]]
    k = 3
    print("---------->", sol.maxSumSubmatrix(matrix, k))
    matrix = [[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]]
    k = 10
    print("---------->", sol.maxSumSubmatrix(matrix, k))
    matrix = [[2,2,-1]]
    k = 0
    print("---------->", sol.maxSumSubmatrix(matrix, k))
    matrix = [[2,2,-1]]
    k = 3

    print("---------->", sol.maxSumSubmatrix(matrix, k))
    print(sol.prefix_sum([2, -3, 9, 1], 10))
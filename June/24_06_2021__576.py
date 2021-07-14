from pprint import pprint
import numpy as np
import time

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        leaf_states = []
        i = 0
        while i in range(m+1):
            row_leaves = []
            j = 0
            while j in range(n+1):
                moves_for_coord = []
                k = 0
                while k in range(maxMove + 1):
                    if k == 0:
                        moves_for_coord.append([((startRow, startColumn), 1)])
                    else:
                        moves_for_coord.append(())
                    k += 1
                row_leaves.append(moves_for_coord)
                j += 1
            leaf_states.append(row_leaves)
            i += 1
        ans_states = [[ [0] * (maxMove + 1) ] * n] * m
        leaf_states, ans_states = self.helper(m, n, (startRow, startColumn), maxMove, leaf_states, ans_states)
        return ans_states[startRow][startColumn][-1] % (pow(10, 9) + 7)
    
    def helper(self, m, n, coord, moves, leaf_states, ans_states):
        if moves == 0:
            return leaf_states, ans_states
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for move in range(1, moves+1):
            pre_leaves = leaf_states[coord[0]][coord[1]][move-1]
            ans = ans_states[coord[0]][coord[1]][move-1]
            curr_leaves = {}
            for item in pre_leaves:
                leaf, leaf_count = item
                for direction in directions:
                    new_leaf = (leaf[0] + direction[0], leaf[1] + direction[1])
                    if new_leaf[0] < 0 or new_leaf[1] < 0 or new_leaf[0] >= m or new_leaf[1] >= n:
                        ans += leaf_count
                    else:
                        if new_leaf in curr_leaves:
                            curr_leaves[new_leaf] += leaf_count
                        else:
                            curr_leaves[new_leaf] = leaf_count
            leaf_states[coord[0]][coord[1]][move] = [(k, v) for k, v in curr_leaves.items()]
            ans_states[coord[0]][coord[1]][move] = ans
        return leaf_states, ans_states

        
if __name__ == "__main__":
    # states[m][n] = [[[leaves], moves]]
    s = Solution()
    m = 7
    n = 6
    maxMove = 13
    startRow = 0
    startColumn = 2
    m = 1
    n = 3 
    maxMove = 3
    startRow = 0 
    startColumn = 1
    s_t = time.time()
    print("jasbdk")
    print(s.findPaths(m, n, maxMove, startRow, startColumn))
    print(f"time taken : {round(1000* (time.time() - s_t))}ms")
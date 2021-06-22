import time 
import heapq
from typing import List

class Solution:     
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        h = [(grid[0][0], 0, 0)]
        output = 0
        visited = set()
        while h:
            elevation, x, y = heapq.heappop(h)
            output = max(output, elevation)
            if (x, y) == (N-1, N-1):
                break
            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < N and 0 <= new_y < N and (new_x, new_y) not in visited:
                    heapq.heappush(h, (grid[new_x][new_y], new_x, new_y))
                    visited.add((new_x, new_y))
        return output
                
if __name__ == '__main__':
    s = Solution()
    nums = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    print(s.swimInWater(nums))
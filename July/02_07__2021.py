import bisect
from typing import List

class Solution:

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.append(float("inf"))
        arr.insert(0, float("-inf"))

        idx = bisect.bisect_left(arr, x)
        if arr[idx-1] < arr[idx]:
            idx -= 1
        i = 0
        ans = []
        while i < k:
            if abs(x - arr[idx]) > abs(x - arr[idx + 1]):
                ans.append(arr.pop(idx + 1))
            else:
                ans.insert(0, arr.pop(idx))
                idx = idx - 1
            i += 1
        return ans[:k]

if __name__ == "__main__":
    sol = Solution()
    # arr = [1,2,3,4,5,6,7,8]
    # k = 4
    # x = 5
    # arr = [1,2,3,4,5]
    # k = 4
    # x = 3
    arr = [0,0,1,2,3,3,4,7,7,8]
    k = 3
    x = 5
    print(sol.findClosestElements(arr, k, x))
        
        
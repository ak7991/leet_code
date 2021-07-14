from typing import List
import bisect

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        rev_arr = []
        ans = []
        for num in nums[::-1]:
            i = bisect.bisect_left(rev_arr, num)
            rev_arr.insert(i, num)
            ans.insert(0, i)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.countSmaller([5,2,6,1]))
    print(sol.countSmaller([-1]))
    print(sol.countSmaller([-1, -1]))
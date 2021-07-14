import time
from typing import List

class Solution:
    def checkLocalMaxima(self, arr, idx):
        # print(idx, len(arr))
        if ((idx <= 0) or (arr[idx - 1] < arr[idx])) and ((idx >= len(arr)-1) or arr[idx] > arr[idx + 1]):
            return True
        else:
            return False

    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.insert(0, float("-inf"))
        nums.append(float("-inf"))
        # Check first element
        if self.checkLocalMaxima(nums, 1):
            return 0
        # Check last element
        elif self.checkLocalMaxima(nums, n):
            return n - 1        
        l = 1
        r = n
        m = (l + r) // 2
        while True:
            ans = self.checkLocalMaxima(nums, m)
            if ans:
                return m - 1
            # go left
            if nums[m - 1] < nums[m + 1]:
                l = m
                m = (m + r) // 2
            # go right
            else:
                r = m
                m = (l + m) // 2

if __name__ == "__main__":
    sol = Solution()
    print(sol.findPeakElement([1,2,1,2,1]))
import bisect
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        last_ele = []
        sub_len = []
        max_len = 0

        for num in nums:
            idx = bisect.bisect_left(last_ele, num)
            # Generate new subsequence
            if num == 0:
                last_ele.insert(0, num)
                sub_len.insert(0, 1)
            else:
                last_ele[idx] = num
                sub_len[idx] += 1
            max_len = max(max_len, sub_len[idx])
        return max_len
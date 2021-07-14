from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = slow = fast = 0
        mem = []
        i = 0
        k_left = k
        while i < len(nums):
            # 1s chunk finish
            if nums[i] == 0 and i > 0 and nums[i-1] == 1:
                if mem == []:
                    pass
                else:
                    # Flip bit
                    if k_left > 0:
                        k_left -= 1
                        max_len = max(max_len, i - mem[0])
                    # No flippable bits left
                    else:
                        mem = []
                        prev_start = mem.pop(0)
                        slow = prev_start[0]
                        if mem != []:
                            current_k = mem[0][1]
                        else:
                            current_k = 0
                        k_left += prev_start[1] - current_k

            # new 1s chunk start
            if nums[i] == 1 and (i == 0 or nums[i - 1] == 0):
                mem.append((i, k_left))
        return max_len

        
    def helper(nums, start, k_left):
        chunks = []
        i = start
        while i < len(nums):
            if nums[i] == 0:
                if k_left > 0:
                    k_left -= 1
                else:
                    break
            i += 1
        return i, k_left



if __name__ == '__main__':
    sol = Solution()
    print(sol.longestOnes())
        
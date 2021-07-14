from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        # open_arrays = []
        ans = 0
        last_legitimate_num = 0
        last_illegitmate_num = 0
        for i, num in enumerate(nums):
            j = i + 1
            if num > right:
                last_illegitmate_num = j
            else:
                if num <= right and num >= left:
                    last_legitimate_num = j
                ans += max(last_legitimate_num - last_illegitmate_num, 0)
            print("last_legitimate_num", last_legitimate_num, "last_illegitmate_num", last_illegitmate_num, "ans", ans)
            # # introduce new open 
            # if num <= right:
            #     open_arrays.append((num, i))
            #     # close "closeable" open arrays
            #     i = 0
            #     while i < len(open_arrays):
            #         # Update max if possible:
            #         if open_arrays[i][0] < num:
            #             open_arrays[i] = (num, open_arrays[i][1])
            #         # if max > left
            #         if open_arrays[i][0] >= left:
            #             ans += 1
            #         i += 1
            #         print(">>",i, open_arrays, ans)

            # # terminate all open arrays
            # else:
            #     open_arrays = []
        print(ans)
        return ans

if __name__ == "__main__":
    s = Solution()
    # nums = [2, 1, 4, 3]
    # left = 2
    # right = 3
    # nums = [3,4,2,24,45,3,2,1,4,6, 1, 4, 3]
    # left = 12
    # right = 40
    nums = [73,55,36,5,55,14,9,7,72,52]
    left = 32
    right = 69
    print(s.numSubarrayBoundedMax(nums, left, right))
import bisect
from typing import List

class Solution:
    def update_element(self, arr, old_element):
        target = bisect.bisect_left(arr, old_element)
        # Direct update
        if target == len(arr) or arr[target + 1] <= arr[target] + 1:
            arr[target] += 1
        else:
            element = arr.pop(target)
            idx = target
            while idx + 1 < len(arr) and arr[idx] == arr[idx + 1]:
                idx += 1
            arr.insert(target + 1, element)
        return arr

    def minSetSize(self, arr: List[int]) -> int:
        ch_map = {}
        occ_arr = []
        for num in arr:
            if num not in ch_map:
                ch_map[num] = 1
                occ_arr.insert(0, 1)
            else:
                occ_arr = self.update_element(occ_arr, ch_map[num])
                ch_map[num] += 1

        arr_len = len(arr)
        rem_len = 0
        idx = 0
        while rem_len < arr_len // 2:
            rem_len += occ_arr[idx]
            idx += 1
        return idx
            




class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start_d = {}
        end_d = {}
        ans = 0
        for num in nums:
            pred_num = num - 1
            succ_num = num + 1
            if (num in start_d) or (num in end_d):
                continue
            else:
                # Mergeable
                if pred_num in end_d and succ_num in start_d:
                    l_l = end_d.pop(pred_num)
                    r_r = start_d.pop(succ_num)
                    start_d[l_l] = r_r
                    end_d[r_r] = l_l
                    ans = max(ans, l_l - r_r + 1)
                elif pred_num in end_d:
                    l_l = end_d.pop(pred_num)
                    start_d[l_l] = num
                    end_d[num] = l_l
                    ans = max(ans, l_l - num + 1)
                elif succ_num in start_d:
                    r_l = start_d.pop(succ_num)
                    end_d[r_l] = num
                    start_d[num] = r_l
                    ans = max(ans, num - r_l + 1)
                else:
                    start_d[num] = num
                    end_d[num] = num
                    ans = max(ans, 1)
                    s_e = end_d[pred_num][0]
                    _len = end_d[pred_num][1] + 1
                    start_d[s_e][0] = num
                    start_d[s_e][1] = end_d[pred_num][1] = _len
                    ans = max(ans, _len)
        return ans
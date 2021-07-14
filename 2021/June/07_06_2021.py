from typing import List

class Solution:
    def helper(self, mod_cost, i=0):
        _arr = mod_cost[i: i + 3]
        if i + 2 == len(mod_cost) - 1:
            return [_arr[1], _arr[0] + _arr[1], _arr[0] + _arr[2]]
        else:
            ans = self.helper(mod_cost, i + 1)
            pref_cost = min(ans[1:])
            return [pref_cost, pref_cost + _arr[0], ans[0] + _arr[0]]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        ans = self.helper(cost)
        return min(ans)
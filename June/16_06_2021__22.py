from typing import List

class Solution:          
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(target, curr_string="", _open=0, _close=0):
            if _close == target:  # all brackets closed
                ans.append(curr_string)
            if _open < target:  # room for more open brackets
                new_curr_string = curr_string +  "("
                dfs(target, new_curr_string, _open+1, _close)
            if _open > _close:  # close brackets allowed; open are more
                new_curr_string = curr_string + ")"
                dfs(target, new_curr_string, _open, _close+1)            
        dfs(n)
        return ans
from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        init_code = [0]
        i = 0
        while i <= n:
            sumCoeff = pow(2, i)
            new_array = [j + sumCoeff for j in init_code[::-1]]
            init_code = init_code + new_array
            i += 1
        return init_code
if __name__ == "__main__":
    sol = Solution()
    print(sol.grayCode(2))

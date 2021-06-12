from typing import List
import numpy as np

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        memo = np.full((len(stones), len(stones)), -1)
        return self.pop_it(0, len(stones) - 1, stones, memo, sum(stones))

    def pop_it(self, start, end, stones, memo, _sum, p=True):
        print(start, end, _sum)
        if start == end:
            return 0
        # print(memo)
        elif end - start == 1:
            print(f"just computed {start, end}: { max(stones[start], stones[end])}")
            memo[start][end] = max(stones[start], stones[end])
        elif memo[start][end] == -1:
            l = _sum - stones[start] - self.pop_it(start + 1, end, stones, memo, _sum - stones[start], p)
            r = _sum - stones[end] - self.pop_it(start, end - 1, stones, memo, _sum - stones[end], p)

            curr_ans = max(l, r)
            print(f"just computed {start, end}: {curr_ans}")
            memo[start][end] = curr_ans
        else:
            print(memo)
            print(f"already computed {start, end}: {memo[start][end]}")
        print(f"curr_ans {(start, end)}", memo[start][end])
        return memo[start][end]
if __name__ == "__main__":
    s = Solution()
    print(s.stoneGameVII([5,3,1,4,2]))
    # print(s.stoneGameVII([7,90,5,1,100,10,10,2]))
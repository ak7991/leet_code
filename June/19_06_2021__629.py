import numpy as np
from typing import List

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if (n < 1 or k < 0):
            return 0

        dp = np.full((n+1, k+1), 0)
        M = 1000000007

        dp[0][0] = 1
        for i in range(1, n+1):
            dp[i][0] = 1
            for j in range(1, k+1):
                if(j < i):
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % M
                else:
                    dp[i][j] = ((dp[i][j - 1] - dp[i - 1][j - i])%M + (dp[i-1][j] +M)%M) % M
        return dp[n][k]

if __name__ == '__main__':
    s = Solution()
    print(s.kInversePairs(10, 2))        
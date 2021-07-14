from typing import List
import time

class Solution:

    def helper(self, matchsticks, sides, match_index=0, depth=0, side_len=0):
        if sides[0] == 0 and sides[1] == 0 and sides[2] == 0 and sides[3] == 0:
            return True
        # if match_index >= len(matchsticks):
        #     return False
        i = 0
        while i < 4:
            # time.sleep(0.01)
            if matchsticks[match_index] <= sides[i]:
                # print("found sum @ depth ", "___"* depth)
                sides[i] -= matchsticks[match_index]
                possible_permutation = self.helper(matchsticks, sides, match_index+1, depth+1, side_len=side_len)
                if possible_permutation:
                    return True
                # print("backtrack @ depth ", "___"* depth)
                sides[i] += matchsticks[match_index]
            i += 1
        return False
            
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False
        # matchsticks.sort()
        return self.helper(matchsticks, [perimeter/4]*4, side_len=perimeter/4)
    
if __name__ == "__main__":
    s = Solution()
    # matchsticks = [1,1,2,2,2]
    # matchsticks = [1,1,1,1,1,1, 1,1,3,3,3,3,4]
    # matchsticks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    matchsticks = [1569462,2402351,9513693,2220521,7730020,7930469,1040519,5767807,876240,350944,4674663,4809943,8379742,3517287,8034755]
    s_t = time.time()
    print(s.makesquare(matchsticks))
    print(f"took {round((time.time() - s_t)*1000)}ms")


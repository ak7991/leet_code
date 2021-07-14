from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        ratings = [ratings[0]] + ratings + [ratings[-1]]
        # Local maxima/minima
        tangents = [(0, -1)]
        i = 1
        while i < len(ratings) - 1:
            # Maxima found
            if ratings[i - 1] < ratings[i] > ratings[i + 1]:
                tangents.append((i, 1))
            # Minima found
            elif ratings[i - 1] >= ratings[i] <= ratings[i + 1]:
                tangents.append((i, -1))
            i += 1
        candies = 0
        tangents.append((i+1, -1))
        for idx, tangent in enumerate(tangents):
            if tangent[1] == 1:
                if tangents[idx - 1][1] == -1:
                    left_terms = tangents[idx][0] - tangents[idx - 1][0] + 1
                else:
                    left_terms = 0
                if tangents[idx + 1][1] == -1:
                    right_terms = tangents[idx + 1][0] - tangents[idx][0] + 1
                else:
                    right_terms = 0
                candies += max(right_terms, left_terms) * (max(right_terms, left_terms) + 1) / 2
                candies += (min(right_terms, left_terms) - 1) * min(right_terms, left_terms) / 2
            elif tangent[1] == -1 and idx not in [0, len(tangents)]:
                # Surrounded by 
                if tangents[idx - 1][1] == -1 and tangents[idx + 1][1] == -1:
                    candies += 1
        return candies

if __name__ == "__main__":
    sol = Solution
    print(sol.candy([1, 2, 1]))
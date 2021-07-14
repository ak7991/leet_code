from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_boxes = sorted(boxTypes, key=lambda x:x[1], reverse=True)
        ans = i = 0
        while truckSize > 0:
            box = sorted_boxes[i]
            take_boxes = min(box[0], truckSize)
            ans += take_boxes * box[1]
            truckSize -= take_boxes
            i += 1
        return ans

if __name__ == "__main__":
    s = Solution()
    boxTypes = [[1,3],[2,2],[3,1]]
    truckSize = 4
    boxTypes = [[5,10],[2,5],[4,7],[3,9]]
    truckSize = 10
    print(s.maximumUnits(boxTypes, truckSize))

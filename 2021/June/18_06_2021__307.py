from typing import List

class SegmentTreeNode:
    def __init__(self, cum_sum, influence, left=None, right=None) -> None:
        self.cum_sum = cum_sum
        self.influence = influence
        self.left = left
        self.right = right

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cum_sum = []
        for i in self.nums:
            self.cum_sum.append(self.cum_sum[-1] + i)
        self.root_node = None
        self.buildTree()

    def buildTree(self):
        root = SegmentTreeNode(self.cum_sum[-1], (0, len(self.cum_sum)), None, None)
        l_n = self.buildTree(self.cum_sum[:len(self.cum_sum)//2])
        r_n = self.buildTree(self.cum_sum[len(self.cum_sum)//2:])
        root.left = l_n
        root.right = r_n
        self.root_node = root

    def traverseToTarget(self, target, delta=0):
        node = self.root_node
        while node.influence != (target, target):
            node.cum_sum += delta
            # go left
            if target < (node.influence[1] - node.influence[0]) // 2:
                node = node.left
            # go right
            else:
                node = node.right

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.traverseToTarget(index, delta)
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        left_chunk = self.traverseToTarget(left)
        right_chunk = self.traverseToTarget(right)
        return right_chunk - left_chunk


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

if __name__ == "__main__":
    ops = ["NumArray","update","update","update","update","update","sumRange"]
    vals = [[[1,2,3,4,5,6,7,8,9,10]],[1,3],[2,2],[7,3],[5,3],[2,8], [2,9]]
    n = NumArray(vals[0][0])
    vals = vals[1:]
    for i, op in enumerate(ops[1:]):
        if op == "sumRange":
            print(n.sumRange(vals[i][0], vals[i][1]))
        if op == "update":
            pass
            n.update(vals[i][0], vals[i][1])
    print(n.root_node)
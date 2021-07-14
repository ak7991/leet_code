from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, preorder, inorder):
        # leaf node reached (in previous recursive call)
        if len(preorder) == 0:
            return None
        node = TreeNode(val=preorder[0])
        relative_root_index = inorder.find(node.val)
        node.left = self.helper(preorder[1:relative_root_index+1], inorder[:relative_root_index])
        node.right = self.helper(preorder[relative_root_index+2:], inorder[relative_root_index+1:])
        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        root = self.helper(preorder, inorder)
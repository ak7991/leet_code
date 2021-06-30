# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        if node.val in [p.val, q.val]:
            return node
        nodeVals = [p.val, q.val]
        nodeStack = [root]
        traversed = []
        currLevel = [[], []]
        while nodeStack != [] or currLevel != [[], []]:
            if nodeStack == []:
                nodeStack = currLevel[0].copy()
                traversed.append(currLevel[1])
                currLevel = [[], []]
            node = nodeStack.pop()
            if node.val in nodeVals:
                nodeVals.remove(node.val)
                break
            else:
                if node.left:
                    currLevel[0].append(node.left)
                if node.right:
                    currLevel[0].append(node.right)
                currLevel[1].append(node)
        while True:
            secondStop = self.findNodes(node, nodeVals)
            # Jack node up
            if secondStop is None:
                possParents = traversed.pop()
                # Finding parent from prev level
                for possParent in possParents:
                    if possParent.left and possParent.left.val == node.val:
                        parent = possParent
                        parent.left = None  # remove the branch already iterated
                    elif possParent.right and possParent.right.val == node.val:
                        parent = possParent
                        parent.right = None  # remove the branch already iterated
                node = parent
                if node.val == root.val:
                    return root
            else:
                return node

    def findNodes(self, startNode, nodeVals):
        nemo = None  # node to find
        nodeStack = [startNode]
        while nodeStack:
            node = nodeStack.pop()
            if node.left:
                if node.left.val in nodeVals:
                    nemo = node
                    break
                else:
                    nodeStack.append(node.left)
            if node.right:
                if node.right.val in nodeVals:
                    nemo = node
                    break

                else:
                    nodeStack.append(node.right)
        return nemo
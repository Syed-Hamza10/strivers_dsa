# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.left == None and root.right == None:
            return root.val

        a = self.evaluateTree( root.left )
        b = self.evaluateTree(root.right)

        if root.val == 2:
            return a or b
        return a and b
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        height, diameter = self.helper(root)
        return diameter
    def helper(self, root):
        if root is None:
            return 0, 0
        lh, ld = self.helper(root.left)
        rh, rd = self.helper(root.right)
        h = max(lh, rh) + 1
        d = max(lh + rh, ld, rd)
        return h, d


        
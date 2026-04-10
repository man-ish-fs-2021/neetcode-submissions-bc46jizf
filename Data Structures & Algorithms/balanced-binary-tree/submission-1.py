# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        h, isBal = self.helper(root)
        return isBal
        

    def helper(self, root):
        if root is None:
            return 0, True
        lh, isLeftBal = self.helper(root.left)
        rh, isRightBal = self.helper(root.right)
        h = max(lh, rh) + 1
        if abs(lh - rh) > 1:
            return h, False
        return h, isLeftBal and isRightBal


        
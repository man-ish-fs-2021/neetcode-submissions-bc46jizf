# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# need to check left height, right height for each element, and see if they match

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        lh = self.height(root.left)
        rh = self.height(root.right)
        if(abs(lh - rh) > 1):
            return False
        leftBal = self.isBalanced(root.left)
        rightBal = self.isBalanced(root.right)
        return leftBal and rightBal

    def height(self, root):
        if root is None:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        return lh + 1 if lh > rh else rh + 1
    
        
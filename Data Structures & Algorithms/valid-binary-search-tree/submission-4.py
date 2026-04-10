# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# brute force is to recursively check the left and right vals (like the )
# need functions for finding the min and max in the particular branch.
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkBst(root)

    def maxTree(self, root):
        if not root:
            return -1000000
        left = self.maxTree(root.left)
        right = self.maxTree(root.right)
        return max(left,right,root.val)
    def minTree(self, root):
        if not root:
            return 1000000
        left = self.minTree(root.left)
        right = self.minTree(root.right)
        return min(left,right,root.val)
    
    def checkBst(self, root):
        if not root:
            return True
        leftMax = self.maxTree(root.left)
        rightMin = self.minTree(root.right)
        if leftMax >= root.val or rightMin <= root.val:
            return False
        isLeftBst = self.checkBst(root.left)
        isRightBst = self.checkBst(root.right)
        return isLeftBst and isRightBst


        

        
        
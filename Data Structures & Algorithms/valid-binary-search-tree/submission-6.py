# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isBST(root, -1000000, 1000000)
    def isBST(self, node, left, right):
        if not node:
            return True
        if not (left < node.val < right):
            return False
        isLeft = self.isBST(node.left, left, node.val)
        isRight = self.isBST(node.right, node.val, right);
        return isLeft and isRight

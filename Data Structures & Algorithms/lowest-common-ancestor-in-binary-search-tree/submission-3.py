# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# basically we are finding the nodes between the two node, including the numbers themselves
# we need to find the lowest number among these
# This is a BST, so the smaller numbers are on the left, 
# Brute force way to do this, find all the elements between these two elements
# if no elemnts between, then consider the p and 1 itslef
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None or not p or not q:
            return None
        return self.helper(root,p,q)
 

    def helper(self, root, p, q):
        if root is None or not p or not q:
            return None
        if (root.val < min(p.val, q.val)):
            return self.helper(root.right, p, q)
        elif (root.val > max(p.val, q.val)):
            return self.helper(root.left,p,q)
        else:
            return root



        
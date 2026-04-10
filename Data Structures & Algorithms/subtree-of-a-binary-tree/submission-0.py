# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# brute way is to go to every node and check if the right and left of the node are matching
# this is only if the roots are matching. 

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        # need to check if the check tree works
        if self.checkTree(root, subRoot):
            return True
        # if the check tree doesnt work, need to check for the left and right 
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    
    def checkTree(self, root1, root2):
        if not root1 and not root2:
            return True
        if root1 and root2 and root1.val == root2.val:
            return (self.checkTree(root1.left, root2.left)) and (self.checkTree(root1.right, root2.right))
        return False
        
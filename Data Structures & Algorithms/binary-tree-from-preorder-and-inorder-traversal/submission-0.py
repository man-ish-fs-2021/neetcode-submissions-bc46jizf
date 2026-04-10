# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#       1 (Root)
#      / \
#     2   3
#    / \
#   4   5
# PRE: 1, 2, 4, 5, 3
# IN: 4,2,5,1,3
# Post: 4,5,2,3,1
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        rootEle = preorder[0]
        print(inorder, rootEle)
        rootIdx = inorder.index(rootEle)
        leftTreeInOrder = inorder[:rootIdx]
        rightTreeInOrder = inorder[rootIdx+1:]
        leftInOrderLen = len(leftTreeInOrder);
        leftTreePreOrder = preorder[1:leftInOrderLen + 1]
        rightTreePreOrder = preorder[leftInOrderLen + 1:]
        root = TreeNode(rootEle)
        root.left = self.buildTree(leftTreePreOrder, leftTreeInOrder)
        root.right = self.buildTree(rightTreePreOrder, rightTreeInOrder)
        return root



        
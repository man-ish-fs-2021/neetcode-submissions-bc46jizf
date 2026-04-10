# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        op = []
        while queue:
            temp = []
            currLen = len(queue)
            for i in range(currLen):
                curr = queue.pop(0)
                if curr:
                    temp.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
            if temp:
                op.append(temp)


        return op



        
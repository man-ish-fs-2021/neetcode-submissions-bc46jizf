# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# need to check each node and check if is same,
# brute way is to go through each node of each tree and equate it
# also can be done with bfs, by checking each node
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        stack = [(p, q)]

        while stack:
            pnode, qnode = stack.pop()
            if not pnode and not qnode:
                continue
            if not pnode or not qnode or pnode.val != qnode.val:
                return False
            stack.append((pnode.right,qnode.right))
            stack.append((pnode.left,qnode.left))
        return True





        
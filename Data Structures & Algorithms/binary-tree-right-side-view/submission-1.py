# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# this might be solved level oreder traversal, and the last element in the nested list

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        op = []
        def mapItems(item):
            print(item)

        while queue:
            currLen = len(queue)
            temp = []
            for i in range(currLen):
                curr = queue.pop(0);
                if not curr:
                    continue
                temp.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if temp:
                op.append(temp)
        print(op)
        return [sub[-1] for sub in op if sub]
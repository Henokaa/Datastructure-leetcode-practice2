# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        answer = []
        def dfs(root, elements):
            if not root:
                return None

            left = dfs(root.left, elements + str(root.val)) 
            right = dfs(root.right, elements + str(root.val))

            if not left and not right:
                str_copy = elements
                answer.append(str_copy + str(root.val))
            
            return root

        dfs(root, "")
        number = 0
        for items in answer:
            number += int(items)
            
        return number
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def dfs(root, path):
            if not root:
                return None
            
            if not root.left and not root.right:
                element = ''.join(map(str, path))
                element += str(root.val)
                # print(element)
                self.total += int(element)
                
            path.append(root.val)
            left = dfs(root.left, path)
            path.pop()
            path.append(root.val)
            right = dfs(root.right, path)
            path.pop()
        
        dfs(root, [])
        return self.total
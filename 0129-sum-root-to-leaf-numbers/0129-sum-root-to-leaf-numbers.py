# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        '''
        sting
        
        dfs()
        
        left = dfs(x + str(root.val))
        roght = dfs(x + str())
        
        if not leave
            sum += 
        '''
        self.total = 0
        def dfs(root, numbers):
            if not root:
                return None
            
            left = dfs(root.left, numbers + str(root.val))
            right = dfs(root.right, numbers + str(root.val))
            
            if not left and not right:
                numbers += str(root.val)
                # print(numbers)
                self.total += int(numbers)
                 
            return root
            
            
            
        dfs(root, "")
        return self.total
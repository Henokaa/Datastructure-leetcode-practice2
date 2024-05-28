# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        '''
        dfs(i)
        
            
        '''
        stack = []
        answer = []
        def dfs(root):
            if not root:
                return None
            
            stack.append(root.val)
            left = dfs(root.left)
            right = dfs(root.right)
            
            
            if not left and not right:
                temp = [str(elements) for elements in stack]
                answer.append("->".join(temp))
                
            
            stack.pop()
            return root
        dfs(root)
        return answer
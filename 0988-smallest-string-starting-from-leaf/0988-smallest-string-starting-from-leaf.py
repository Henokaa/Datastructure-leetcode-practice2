# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        '''
        
        dfs()
            leaf
            flip string
            append
        
        sort
        [0]
        '''
        
        temp = []
        
        def dfs(root, path):
            if not root:
                return
            
            path.append(chr(97 + root.val))
            left = dfs(root.left, path)
            right = dfs(root.right, path)
            
            if left == None and right == None:
                temp.append(path[::-1].copy())
                
            path.pop()
            return root
        
        
        dfs(root, [])
        # print(temp)
        temp.sort()
        
        return ''.join(temp[0])
        
        
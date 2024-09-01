# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        '''
        backtacking
        '''
        ans = []
        def dfs(root, path):
            if not root:
                return None
            
            path.append(root.val)
            left = dfs(root.left, path)
            right = dfs(root.right, path)
            
            
            if left == None and right == None:
                ans.append(path.copy())
                
            path.pop()
            return root
        
        dfs(root, [])
        
        # Very Very important, this or you can add str in the parameter of the function(see different solution)
        solution = 0
        for i in range(len(ans)):
            temp = ''.join(map(str, ans[i]))
            solution += int(temp)
            
        return solution
        
        # row = ''
        # cols = 0
        # for x in range(len(ans)):
        #     for y in range(len(ans[x])):
        #         row += str(ans[x][y])
        #     # print(row)
        #     cols += int(row)
        #     row = ''
        # return cols
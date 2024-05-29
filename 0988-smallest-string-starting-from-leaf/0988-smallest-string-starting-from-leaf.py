# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        '''
        go to the bottom 
        sort all the leaf output
        '''
        answer = []
        def dfs(root, path):
            if not root:
                return root
            
            path.append(root.val)
            left = dfs(root.left, path)
            
            right = dfs(root.right, path)
            
            
            if not left and not right:
                
                temp = [chr(65 + int(elem)) for elem in path]
                temp = temp[::-1]
                # print(temp)
                answer.append(temp)
            
            path.pop()
            
            return root
                
        
        dfs(root, [])
        answer.sort()
        text = "".join(answer[0])
        return text.lower()
        print(answer)
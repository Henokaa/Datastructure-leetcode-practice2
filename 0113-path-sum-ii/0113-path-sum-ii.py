# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer = []
        def dfs(root, stack):
            # print(root.val)
            if not root:
                return
            stack.append(root.val)
            if not root:
                return
            if not root.left and not root.right:
                if sum(stack) == targetSum: 
                    answer.append(stack.copy())
            
            left = dfs(root.left, stack)
            right = dfs(root.right, stack)
            stack.pop()
        dfs(root, [])
        return answer
            
        
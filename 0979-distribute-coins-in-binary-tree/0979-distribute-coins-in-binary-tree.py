# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0
            
            left_balance = dfs(node.left)
            right_balance = dfs(node.right)
            
            # Total moves is the sum of absolute balances from left and right
            moves[0] += abs(left_balance) + abs(right_balance)
            
            # Balance of this node
            return node.val + left_balance + right_balance - 1

        moves = [0]
        dfs(root)
        return moves[0]
        
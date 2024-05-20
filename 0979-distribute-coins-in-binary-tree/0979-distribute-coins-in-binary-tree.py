# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        '''
        Key Observations:
Total Coins and Nodes Match: Since the total number of coins equals the total number of nodes, the goal is to distribute the coins such that each node ends up with exactly one coin.
Excess and Deficit:
A node with more than one coin (excess) needs to give away coins.
A node with zero coins (deficit) needs to receive coins.
Net Balance: The net balance of coins for a node is defined as number of coins - 1. This tells us whether a node has excess coins (positive balance) or needs coins (negative balance).
        '''
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
        
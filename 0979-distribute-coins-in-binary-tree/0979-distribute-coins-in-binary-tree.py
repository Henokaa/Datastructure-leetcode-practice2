# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        Bucket = namedtuple('Bucket', ['coins', 'total'])
        
        def traverse(node):
            if node is None:
                return Bucket(0,0)
            
            left = traverse(node.left)
            right = traverse(node.right)
            
            total = left.total + right.total
            delta = left.coins + right.coins + (node.val - 1)
            
            total += abs(delta)
            
            return Bucket(delta, total)
        
        ans = traverse(root)
        return ans.total
        
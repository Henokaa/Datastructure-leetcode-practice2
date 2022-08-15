# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(root, prev):
            if not root:
                return
            if root.val >= prev:
                self.count += 1
            prev = max(prev, root.val)
            left = dfs(root.left, prev)
            right = dfs(root.right, prev)
            return
        dfs(root, root.val)
        return self.count
            
        return 0
'''space-complexity-o(logn) in other words o(h) which techniquely can be bigger than logn, it can be as big as n'''
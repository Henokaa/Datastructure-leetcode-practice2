# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxD(rt):
            nonlocal diameter
            if not rt:
                return 0

            left = maxD(rt.left)
            right = maxD(rt.right)
            diameter = max(left + right, diameter)
            return max(left, right) + 1

        diameter = 0
        maxD(root)
        return diameter
        
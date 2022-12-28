# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder - root, left, right
        # [3,9,20,15,7]
        # inorder - left, root, right
        # [9,3,15,20,7]
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        indexs = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:1 + indexs], inorder[:indexs])
        root.right = self.buildTree(preorder[1 + indexs:], inorder[indexs+1:])
        return root
        
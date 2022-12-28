# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        '''
        The easiest way to do it is to do it for the root, because its not cut
        inorder - left, root, right
        [9,3,15,20,7]
        postorder - left, right, root
        [9,15,7,20,3]
        '''
        if not postorder or not inorder:
            return None
        
        root = TreeNode(postorder[-1])
        indexs = inorder.index(postorder[-1])
        
        root.left = self.buildTree(inorder[:indexs], postorder[:indexs])
        root.right = self.buildTree(inorder[indexs + 1:], postorder[indexs:-1])
        return root
        
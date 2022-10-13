# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        self.right = None
        if not root:
            return root
        
        
        def dfs(root):
            if not root:
                return root
            if key > root.val:
                root.right = dfs(root.right)
            if key == root.val:
                if root.right:
                    self.right = root.right
                # if root.left: this wiil cause error
                '''
                [5,3,6,2,4,null,7]
                7
                '''
                return root.left
            if key < root.val:
                root.left = dfs(root.left)
            return root
        def BST(root):
            if not root:
                return self.right
            if root.val < self.right.val:
                root.right = BST(root.right)
            else:
                root.left = BST(root.left)
            return root
            # if not root:
            #     return self.right
            # if self.right.val > root.val:
            #     if not root.right:
            #         root.right = self.right
            #     BST(root.right)
            # if self.right.val < root.val:
            #     if not root.left:
            #         root.left = self.right
            #     BST(root.left)
            
        '''
        to handle this test case - [0] 0
        '''
        if root.val == key:
            self.right = root.right
            
            root = root.left
            if self.right != None:
                return BST(root) 
            ''' There must be a return here otherwise this error
                [1,null,2]
                    1'''
            return root
        
        
        dfs(root)
        if self.right != None:
            BST(root)
        return root
        
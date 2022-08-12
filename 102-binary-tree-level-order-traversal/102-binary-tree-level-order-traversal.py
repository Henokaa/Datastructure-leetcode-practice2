# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = deque()
        que.append(root)
        array = []
        ans = []
        if not root:
            return ans
        while que:
            length = len(que)
            for i in range(length):
                temp = que.popleft()
                if temp:
                    array.append(temp.val)
                    if temp.left:
                        que.append(temp.left)
                    if temp.right:
                        que.append(temp.right)
            ans.append(array)
            array = []
        return ans
            
            
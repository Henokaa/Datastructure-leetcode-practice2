# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        que = deque()
        test = 0
        if not root:
            return ans
        que.append(root)
        ans.append(root.val)
        while que:
            length = len(que)
            for i in range(length):
                temp = que.popleft()
                if temp.right:
                    que.append(temp.right)
                if temp.left:
                    que.append(temp.left)
            if que:
                ans.append(que[0].val)
        return ans
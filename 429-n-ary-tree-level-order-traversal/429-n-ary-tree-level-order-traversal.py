"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        que = deque()
        ans = []
        value = []
        que.append(root)
        while que:
            l = len(que)
            for i in range(l):
                temp = que.popleft()
                value.append(temp.val)
                for x in temp.children:
                    que.append(x)
                    
            ans.append(value)
            value = []
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.graph = defaultdict(list)
        if k == 0:
            return [target.val]
        def dfs(root):
            if not root:
                return
            if root.left:
                left = root.left 
                self.graph[root.val].append(left.val)
                self.graph[left.val].append(root.val)
                dfs(root.left)
                
            if root.right:
                right = root.right
                self.graph[root.val].append(right.val)
                self.graph[right.val].append(root.val)
                dfs(root.right)

        
        dfs(root)
        # print(self.graph)
        que = deque()
        que.append(target.val)
        visited = set()
        visited.add(target.val)
        level = 0
        while que:
            length = len(que)
            for i in range(length):
                temp1 = que.popleft()
                for x in self.graph[temp1]:
                    if x == temp1:
                        continue
                    if x not in visited:
                        que.append(x)
                        visited.add(x)
            level += 1
            if level == k:
                break
        return list(que)
        
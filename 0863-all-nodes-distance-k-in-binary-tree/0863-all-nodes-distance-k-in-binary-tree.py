# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def dfs(root):
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                dfs(root.left)
            
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                dfs(root.right)

        
        dfs(root)
        # print(graph)
        que = deque()
        
        visited = set()
        que.append(target.val)
        visited.add(target.val)
        ans = [target.val]
        while que and k > 0:
            length = len(que)
            
            for _ in range(length):
                output = que.popleft()
                for child in graph[output]:
                    if child not in visited:
                        que.append(child)
                        visited.add(child)
            ans = list(que)
            # print(ans)
            k -= 1
            
        return ans


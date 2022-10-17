class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = Counter()
        queue = deque([])
        answer = [node for node in range(len(quiet))]
        for a, b in richer:
            graph[a].append(b)
            indegree[b] += 1
        print(graph)
        for node in range(len(quiet)):
            if indegree[node] == 0:
                queue.append(node)
        while queue:
            print(queue)
            front = queue.popleft()
            for child in graph[front]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
                if quiet[answer[front]] < quiet[answer[child]]:
                    answer[child] = answer[front]
        return answer
        
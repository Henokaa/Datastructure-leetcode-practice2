class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        queue = collections.deque([''])
        a = s
        for s in a:
            size = len(queue)
            if s.isdigit():
                for _ in range(size):
                    curr = queue.popleft()
                    queue.append(curr + s)
            else:
                for _ in range(size):
                    curr = queue.popleft()
                    queue.append(curr + s.lower())
                    queue.append(curr + s.upper())
        
        return list(queue)
        
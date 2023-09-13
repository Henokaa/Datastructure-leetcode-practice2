class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def dfs(num):
            if num > n:
                return
            result.append(num)
            for digit in range(10):
                if num * 10 + digit > n:
                    return
                dfs(num * 10 + digit)

        for i in range(1, 10):
            dfs(i)

        return result
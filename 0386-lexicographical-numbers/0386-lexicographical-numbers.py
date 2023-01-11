class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def dp(cur):
            
            for i in range(0,10):
                num = str(cur) + str(i)
                if not 1 <= int(num) <= n:
                    break
                ans.append(int(num))
                if 1 <= int(num) * 10 <= n:
                    dp(num)
                
        if n >= 10:
            for i in range(1, 10):
                ans.append(i)
                dp(i)
                
        else:
            for i in range(1, n + 1):
                ans.append(i)
        return ans
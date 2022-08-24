class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dp(cur):
            if cur in memo:
                return memo[cur]
            if cur == s:
                return True
            
            
            for word in wordDict:
                if cur+word != s[:len(cur+word)]:
                    continue
                if dp(cur + word):
                    return True
            
            memo[cur] = False
            return False
            
        memo = {}
        return dp("")
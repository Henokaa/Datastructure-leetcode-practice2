class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dp(cur, path):
            if cur == s:
                res.append(path)
                return
            
            if cur != s[:len(cur)]:
                return 
            
            for word in wordDict:
                path.append(word)
                dp(cur + word , path.copy())
                path.pop()
            
        
        res = []
        dp("", [])
        return [' '.join(res[i]) for i in range(len(res))]
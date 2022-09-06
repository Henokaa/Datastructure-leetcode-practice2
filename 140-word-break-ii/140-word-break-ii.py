class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dp(cur, ans):
            
            if cur == s:
                res.append(ans)
                return 
            for words in wordDict:
                if (cur + words) != s[:len(cur+words)]:
                    continue
                else:
                    dp(cur + words, ans + [words])
                    
                    
        
        res = [] 
        dp("", [])
        
        return [' '.join(res[i]) for i in range(len(res))]
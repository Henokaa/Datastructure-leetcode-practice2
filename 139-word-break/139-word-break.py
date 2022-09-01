class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # brute force  0(n^2)
        '''meaning from the word to the worddict for every word in s'''
        def dp(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True
            for w in wordDict:
                if i+len(w) <= len(s) and s[i:i+len(w)] == w:
                    if dp(i+len(w)):
                        return True
            memo[i] = False
            return False
        memo = {}
        return dp(0)
    # time complexity - 0(n*m*n) the last n for comparing
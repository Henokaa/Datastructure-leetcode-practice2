class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        words.sort(key=len)
        d = {}
        
        for word in words:
            d[word] = 1
            
            for j in range(len(word)):            
                successor = word[:j] + word[j+1:]
                if successor in d:
                    d[word] = max(d[word], 1 + d[successor])

        return max(d.values())      
        
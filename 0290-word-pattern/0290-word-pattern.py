class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        saved = {}
        s = s.split()
        if len(s) != len(pattern):
            return False
        visited = set()
        for i in range(len(pattern)):
            if pattern[i] in saved:
                word1 = saved[pattern[i]]
                word2 = s[i]
                # print(word1, word2)
                if word1 != word2:
                    return False
            else:
                if s[i] in visited:
                    return False
                
                saved[pattern[i]] = s[i]
                visited.add(s[i])
            # print(saved)
        return True
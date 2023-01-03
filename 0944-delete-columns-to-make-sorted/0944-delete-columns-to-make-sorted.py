class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        s = ['' for _ in range(len(strs[0]))]
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                s[j] += strs[i][j]
        # print(s)
        count = 0
        for i in range(len(s)):
            
            temp = ''.join(sorted(s[i]))
            # print(s[i], temp)
            if temp != s[i]:
                count += 1
        return count
        
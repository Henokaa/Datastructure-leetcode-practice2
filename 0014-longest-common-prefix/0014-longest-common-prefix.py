class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        i = 0
        ans = ""
        
        for i in range(len(strs[0])):
            temp = strs[0][i]
            for elem in range(len(strs)):
                if i >= len(strs[elem]) or strs[elem][i] != temp:
                    return ans
            ans += temp
            
        return ans
                    
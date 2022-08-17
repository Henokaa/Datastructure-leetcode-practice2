class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''Time-complexity - o(n^2) because five rows and at max five element
        space - o(n^2)'''
        result = []
        ans = [1]
        
        result.append(ans)
        if numRows == 1:
            return result
        
        
        for i in range(1, numRows):
            ans = [0] + ans + [0]
            l = 0
            r = 1
            while r <= len(ans)-1:
                ans[l] = ans[l] + ans[r]
                l += 1
                r += 1
            ans.pop()
            result.append(ans)
        
        return result
        # for i in range(1, n-1):
        #     ans
        
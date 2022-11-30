class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        saved = {}
        saved[2] = "abc"
        saved[3] = "def"
        saved[4] = "ghi"
        saved[5] = "jkl"
        saved[6] = "mno"
        saved[7] = "pqrs"
        saved[8] = "tuv"
        saved[9] = "wxyz"
        
        def backtrack(z, path, i):
            # print("a", path)
            path.append(z)
            
            if len(path) == len(digits):
                ans.append("".join(path))
                return
            
            if i+1 < len(digits):
                for x in saved[int(digits[i+1])]:
                    backtrack(x, path, i + 1)
                    path.pop()

                    
        ans = []
        if len(digits) > 0:
            for z in saved[int(digits[0])]:
                backtrack(z, [], 0)
        
        return ans
        
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        #base case: if it's a number, return it
        if expression.isnumeric():
            return [int(expression)]
        
        #general case
        res = []
        for i, char in enumerate(expression):
            if char in ['+', '-', '*']:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                
                for le in left:
                    for ri in right:
                        if char == '+':
                            res.append(le + ri)
                        elif char == '-':
                            res.append(le - ri)
                        else: # char == '*'
                            res.append(le * ri)
        return res
        
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            temp = bin(i)
            ans.append(temp.count("1"))
        return ans
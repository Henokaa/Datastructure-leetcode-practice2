class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for x in logs:
            if x == "../":
                if count:
                    count -= 1
            elif x == "./":
                count = count
            else:
                count += 1
                
        return count
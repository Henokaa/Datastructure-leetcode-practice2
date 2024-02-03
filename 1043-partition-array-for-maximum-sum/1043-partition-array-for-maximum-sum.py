class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        '''
        
        Time - 0(n * k)
        space - (n)
        Partition 1: [1, 15, 7] | Partition 2: [9, 2, 5]
        Partition 1: [1, 15] | Partition 2: [7, 9, 2] | Partition 3: [5]
        Partition 1: [1] | Partition 2: [15, 7, 9] | Partition 3: [2, 5]
        '''
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            max_val = 0
            for j in range(1, min(k, i) + 1):
                # print(i,j)
                max_val = max(max_val, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + max_val * j)
        # print(dp)
        return dp[n]
        
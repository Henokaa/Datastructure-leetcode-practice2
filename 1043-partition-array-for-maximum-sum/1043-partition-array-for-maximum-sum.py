class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        '''
        
        Time - 0(n * k)
        space - (n)
        Partition 1: [1, 15, 7] | Partition 2: [9, 2, 5]
        Partition 1: [1, 15] | Partition 2: [7, 9, 2] | Partition 3: [5]
        Partition 1: [1] | Partition 2: [15, 7, 9] | Partition 3: [2, 5]
        '''
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            
            
            cur_max = 0
            res = 0
            for j in range(i, min(i+k, len(arr))):
                cur_max = max(cur_max, arr[j])
                size_max = cur_max * (j - i + 1)
                res = max(res ,dfs(j + 1) + size_max)
            cache[i] = res
            return res

            
            
        return dfs(0)
        
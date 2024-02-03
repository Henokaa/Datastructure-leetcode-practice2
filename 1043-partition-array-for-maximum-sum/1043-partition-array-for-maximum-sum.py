class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        '''
        
        [1,4,1,5,7,3,6,1,9,9,3]
         ^
           ^
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
        
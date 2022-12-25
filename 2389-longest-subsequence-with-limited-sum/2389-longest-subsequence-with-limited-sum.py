class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = []
        run = 0
        for i in range(len(nums)):
            run += nums[i]
            prefix.append(run)
        
        ans = []
        for query in queries:
            l = -1
            r = len(prefix)
            while r > l + 1:
                mid = l + (r-l)//2
                if prefix[mid] == query:
                    l = mid
                    break
                elif prefix[mid] > query:
                    r = mid
                else:
                    l = mid
            ans.append(l + 1)
            
        return ans
                
                
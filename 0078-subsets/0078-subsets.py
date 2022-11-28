class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        [1, 2, 3]
        [1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]
        o(n * 2^n)
        8 choices with n elements max
        '''
        
        def backtrack(start, end, tmp):
            ans.append(tmp[:])
            for i in range(start, end):
                tmp.append(nums[i])
                backtrack(i+1, end, tmp)
                tmp.pop()
        ans = []
        backtrack(0, len(nums), [])
        return ans
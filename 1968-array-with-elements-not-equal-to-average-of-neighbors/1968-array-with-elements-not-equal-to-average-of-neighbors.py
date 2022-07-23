class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        ans = [-1] * len(nums)
        r = 0
        i = 0
        while r <= len(nums) - 1:
            ans[r] = nums[i]
            i += 1
            r += 2

        for x in range(len(ans)):
            if ans[x] == -1:
                ans[x] = nums[i]
                i += 1
        return ans
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # /\/\/\/\
        # \/\/\/\/
        def solve(flag):
            searching_greater = flag
            answer = 0
            last = [float('inf'), float('-inf')][flag]
            # 2 4 1
            for i in range(len(nums)):
                if searching_greater:
                    if nums[i] > last:
                        answer += 1
                        last = nums[i]
                        searching_greater = 1 - searching_greater
                    else:
                        last = min(last, nums[i])
                else:
                    if nums[i] < last:
                        answer += 1
                        last = nums[i]
                        searching_greater = 1 - searching_greater
                    else:
                        last = max(last, nums[i])
            return answer
        return max(solve(1), solve(0))
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def backtrack(currentPerm, remainingNums, res):
            if not remainingNums:
                res.append(currentPerm)

            for i in range(len(remainingNums)):
                if i > 0 and remainingNums[i] == remainingNums[i-1]:
                    continue
                
                if currentPerm and not square(remainingNums[i] + currentPerm[-1]):
                    continue

                backtrack(currentPerm + [remainingNums[i]], remainingNums[:i] + remainingNums[i+1:], res)

        def square(num):
            return pow(int(sqrt(num)), 2) == num

        res = []
        backtrack([], sorted(nums), res)
        print(res)
        return len(res)
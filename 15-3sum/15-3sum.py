class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ''' [-1,0,1,2,-1,-4]
              ^ '''
        num = sorted(nums)
        value = 0
        ans = []
        while value < len(nums) - 1:
            l = value + 1
            r = len(nums) - 1
            if value > 0  and num[value] == num[value - 1]:
                value += 1
                continue
            number = - num[value]
            while l < r:
                if (num[l] + num[r]) == number:
                    ans.append([num[value], num[l], num[r]])
                    l += 1
                    while num[l] == num[l-1] and l<r:
                        l += 1
                    
                elif (num[l] + num[r]) > number:
                    r -= 1
                elif (num[l] + num[r]) < number:
                    l += 1
                    
            value += 1
    
        return ans 
        
    '''
    time - o(nlogn) + o(n**2)
    time - o(n**2)
    space - depends how you implement sort o(1) or o(n)
    you can also do it like if the sum of the two numbers, if the opposite is found that's one answer then putting that in a visited set, space 0(2n) 
    [-1, 0, 1, 2, -1, -4]
      ^                ^ 
      '''
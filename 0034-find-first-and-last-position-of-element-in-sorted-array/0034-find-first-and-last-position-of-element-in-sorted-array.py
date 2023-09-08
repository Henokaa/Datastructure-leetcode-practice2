class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(start):
            l = -1
            r = len(nums)
            begin = -1
            ending = -1
            while r > l + 1:
                mid = l + (r - l) // 2
                if nums[mid] > target:
                    r = mid
                elif nums[mid] < target:
                    l = mid
                else:
                    if start == True:
                        r = mid
                        begin = mid 
                    else:
                        l = mid
                        ending = mid
            
            if start == True:
                return begin
            else:
                return ending
        start = binary_search(True)
        end = binary_search(False)
        # print(start, end)
        return [start, end]
    
    '''
    The most important rule in binary search 
 L = -1 and r = len(nums), this only works for index, and not for like a question koko eating banana. 
 l = mid
 r = mid
 
 but for l <= r where l = 0, r = len(nums) - 1 
 l = mid + 1
 r = mid - 1
    '''
        
        
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = -1
        r = len(arr)
        while r > l + 1:
            mid = l + (r - l) // 2
            if arr[mid] > x:
                r = mid
            elif arr[mid] < x: 
                l = mid
            else:
                l = mid
                
        # print(l,r)
                
        ans = []
        while len(ans) < k:
            if r > len(arr) - 1 or abs(x - arr[l]) <= abs(x - arr[r]):
                ans.append(arr[l])
                l -= 1
            elif l < 0 or abs(x - arr[l]) > abs(x - arr[r]):
                ans.append(arr[r])
                r += 1
        ans.sort()
        return ans
            
                
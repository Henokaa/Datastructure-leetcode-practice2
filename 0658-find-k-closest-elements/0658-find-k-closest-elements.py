class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = -1
        r = len(arr)
        index
        while r > l + 1:
            mid = l + (r - l) // 2
            if arr[mid] ==x:
                r = mid
            elif arr[mid] > x:
                r = mid
            else:
                l = mid
        print(l,r)
        
        ans = []
        while k > 0:
            if r < len(arr) and l > -1 and abs(arr[r] - x) < abs(arr[l] - x):
                ans.append(arr[r])
                r += 1
                k -= 1
            elif k > 0 and l > -1 and r < len(arr) and abs(arr[r] - x) >= abs(arr[l] - x):
                ans.append(arr[l])
                l -= 1
                k -= 1
            elif l > -1 and r >= len(arr):
                ans.append(arr[l])
                l -= 1
                k -= 1
            elif r < len(arr) and l <= -1:
                ans.append(arr[r])
                r += 1
                k -= 1
                
        ans.sort()
        return ans
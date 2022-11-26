class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = -1
        r = len(arr)
        value = float('inf')
        ans = []
        while r > l + 1:
            mid = l + (r - l)// 2
            # print(mid, l, r)
            if arr[mid] > x:
                r = mid
            elif arr[mid] <= x:
                l = mid
        
        # print(l, r)
        while len(ans) < k:
            # print(ans)
            if r > len(arr) - 1 or abs(x - arr[l]) < abs(x - arr[r]) :
                ans.append(arr[l])
                l -= 1
            elif l < 0 or abs(x - arr[r]) < abs(x - arr[l]):
                ans.append(arr[r])
                r += 1
            else:
                ans.append(arr[l])
                l -= 1
        # print(ans)
        ans.sort()
        return ans
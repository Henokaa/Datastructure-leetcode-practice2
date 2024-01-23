class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_length = [0]  
    
        def backtrack(index, curr_string):
            if len(set(curr_string)) != len(curr_string):  
                return

            max_length[0] = max(max_length[0], len(curr_string))  

            for i in range(index, len(arr)):
                backtrack(i + 1, curr_string + arr[i])  
        
        backtrack(0, "")
        return max_length[0]

        
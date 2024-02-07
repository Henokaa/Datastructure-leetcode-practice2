class Solution:
    def frequencySort(self, s: str) -> str:
        letter = defaultdict(int)
        inbound = lambda row, cols: 0 <= row < len(grid) 
        
        
        for char in s:
            letter[char] += 1
        
        # print(letter)
        
        sorted_letter = sorted(letter.items(), key = lambda x:x[1], reverse = True)
        # print(sorted_letter)
        answer = ''
        for x,y in sorted_letter:
            answer += x * y
            
        return answer
            
        
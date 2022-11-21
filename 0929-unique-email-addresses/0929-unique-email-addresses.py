class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        count = 0
        visited = set()
        for string in emails:
            x, y = string.split('@')
            word = ""
            for i in x:
                if i == ".":
                    continue
                elif i == "+":
                    break
                else:
                    word += i
            # print(x,y)
            word += "@"
            word += y
            if word not in visited:
                count += 1
                visited.add(word)
            
        # print(count, visited)
        return count
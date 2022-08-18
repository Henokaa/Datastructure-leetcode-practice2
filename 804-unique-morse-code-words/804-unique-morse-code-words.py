class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        word = ""
        visited = set()
        for i in words:
            for j in i:
                word += alphabet[ord(j)-97]
            visited.add(word)
            word = ""
        
        
        
        return len(visited)
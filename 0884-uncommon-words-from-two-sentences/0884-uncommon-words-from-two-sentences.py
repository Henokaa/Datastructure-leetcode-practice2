class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split(" ")
       
        saved_word = defaultdict(int)
        for i in range(len(words)):
            saved_word[words[i]] += 1
        
        words_2 = s2.split(" ")
        
        saved_word_2 = defaultdict(int)
        for i in range(len(words_2)):
            saved_word_2[words_2[i]] += 1
        
        
        answer = []
        
        for word,freq in saved_word.items():
            if freq == 1:
                if word not in saved_word_2:
                    answer.append(word)
                  
        for word,freq in saved_word_2.items():
            if freq == 1:
                if word not in saved_word:
                    answer.append(word)
                    
        return answer
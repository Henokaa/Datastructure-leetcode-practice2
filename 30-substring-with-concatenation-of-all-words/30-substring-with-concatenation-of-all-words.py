class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # remove empty cases
        if not s or words==[]:
            return []  
        len_str=len(s)
        len_word=len(words[0])
        len_substr=len(words)*len_word

        # creating dict of the number of appearance that should be in s for each word
        appearance={}
        for word in words:
            if word in appearance:
                appearance[word]+=1
            else:
                appearance[word]=1

        ans=[]
        for str_start in range(min(len_word,len_str-len_substr+1)):
            ans += self.findAnswer(str_start,len_word,len_substr,s,appearance)
        return ans


    def findAnswer(self,str_start,len_word,len_substr,s,appearance):
        word_start=str_start
        curr_appearance={}
        res = []

        while str_start + len_substr <= len(s):
            word = s[word_start:word_start+len_word]
            word_start += len_word
            # if we encountered word that is not in words, start checking again
            if word not in appearance:
                str_start=word_start
                curr_appearance.clear()

            else:
                # add the word to the current appearance
                if word in curr_appearance:
                    curr_appearance[word]+=1
                else:
                    curr_appearance[word]=1

                # as long as this word appears in our counting more than it should, 
                # update the substring to be one less word, until we reach to
                # this word (sub 1 from the count of the first word count again)
                while curr_appearance[word] > appearance[word]:
                    curr_appearance[s[str_start:str_start+len_word]]-=1
                    str_start += len_word

                # if we handled the last word missing in substring- we found res!
                if word_start-str_start==len_substr:
                    res.append(str_start)
        return res
        
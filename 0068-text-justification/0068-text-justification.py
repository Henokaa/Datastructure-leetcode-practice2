class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        lines = defaultdict(list)
        lengths = defaultdict(int)
        counter = 0
        width = maxWidth
        
        for i in range(n):
            word = words[i]
            m = len(word)
            
            if m > width:
                width = maxWidth
                counter += 1
            
            lines[counter].append(word)
            lengths[counter] += m
            width = width - (m + 1)
            
        result = []
        l = len(lines)
        
        for key, values in enumerate(lines.values()):
            spaces = len(values) - 1
            width = maxWidth - lengths[key]
            s = ''
            
            if key == l - 1:
                for i, v in enumerate(values):
                    if i == spaces:
                        s += v.ljust(width + len(v))
                    else:
                        s += v + ' '
                        width -= 1
            
            elif spaces == 0:
                s = values[0].ljust(maxWidth)
            
            else:
                for i in range(spaces, -1, -1):
                    s = values[i] + s

                    if i > 0:
                        s = ' ' * (width // i) + s
                        width = width - (width // i)
            
            result.append(s)
                
        return result
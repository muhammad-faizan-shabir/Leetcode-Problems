class Solution:
    def reverseWords(self, s: str) -> str:
        size = len(s)
        i = 0
        l = []

        while(i < size):
            if(s[i] != " "):
                start = i 
                
                while(i < size and s[i]!=" "):
                    i = i + 1
                
                word = s[start:i]
                l.insert(0, word)
            else:
                i = i + 1
        
        reversedStr = " ".join(l)

        return reversedStr
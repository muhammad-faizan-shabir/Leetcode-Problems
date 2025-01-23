class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        char_to_row_mapping={'q' : 1,'w':1,'e':1,'r':1,'t':1,'y':1,'u':1,'i':1,'o':1,'p':1,'a':2,'s':2,'d':2,'f':2,'g':2,'h':2,'j':2,'k':2,'l':2,'z':3,'x':3,'c':3,'v':3,'b':3,'n':3,'m':3}
        solution=[]
       
        for word in words:
            row = char_to_row_mapping[word[0].lower()]
            canBeTyped=True
        
            for char in word:
                if(row!=char_to_row_mapping[char.lower()]):
                    canBeTyped=False
                    break
        
            if(canBeTyped):
                solution.append(word)
        
        return solution
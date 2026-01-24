class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        words = s.split()
        noOfWords = len(words)
        noOfLetters = len(pattern)
        
        if(noOfWords != noOfLetters):
            return False
        
        i = 0
        d1 = {}
        d2 = {}
        
        while(i < noOfLetters):
            letter = pattern[i]
            word = words[i]

            if((letter in d1 and d1[letter] != word) or (word in d2 and d2[word] != letter)):
                return False
            elif(letter not in d1 and word not in d2):
                d1[letter] = word
                d2[word] = letter
            
            i = i + 1
        
        return True
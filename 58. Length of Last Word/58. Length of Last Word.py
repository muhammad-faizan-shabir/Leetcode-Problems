class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        strLength = len(s)

        if(strLength==1):
            if(s[0]==' '):
                return 0
            else:
                return 1
        
        i=strLength-1

        while(i>=0 and s[i]==' '):
            i=i-1
        
        lastWordLength=0

        while(i>=0 and s[i]!=' '):
            i=i-1
            lastWordLength=lastWordLength+1
        
        return lastWordLength

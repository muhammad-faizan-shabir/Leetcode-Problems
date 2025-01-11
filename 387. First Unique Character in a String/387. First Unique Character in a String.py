class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary={}
        size=len(s)

        for i in range(0,size):
            dictionary[s[i]]=dictionary.get(s[i],0)+1
        
        for i in range(0,size):
            if(dictionary[s[i]]==1):
                return i
        
        return -1
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        dictionary={}

        for i in s:
            dictionary[i]= dictionary.get(i,0)+1
        
        for i in t:
            if(i in dictionary):
                dictionary[i]=dictionary[i]-1
            else:
                return False
        
        for i in dictionary:
            if(dictionary[i]!=0):
                return False
        
        return True

        
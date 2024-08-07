class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        size=len(s)
        s2=""

        for i in range(0,size):
            if(s[i].isalnum()):
                s2=s2+ s[i].lower()
        
        size= len(s2)
        i=0
        j=size-1
        validity=True

        while(validity==True and i<j):
            if(s2[i]!=s2[j]):
                validity=False
            i=i+1
            j=j-1
        
        return validity


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sPointer=0
        tPointer=0
        sizeS=len(s)
        sizeT=len(t)

        while(sPointer<sizeS and tPointer<sizeT):
            while(tPointer<sizeT and t[tPointer]!=s[sPointer]):
                tPointer=tPointer+1
            if(tPointer<sizeT):
                tPointer=tPointer+1
                sPointer=sPointer+1
        
        if(sPointer==sizeS):
            return True
        else:
            return False
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        size=len(s)
        preImagesToImages={}
        ImagesToPreImages={}
        keepMoving=True
        i=0
        
        while(keepMoving==True and i<size):
            if((s[i] in preImagesToImages)):
                if((preImagesToImages[s[i]]!=t[i])):
                    keepMoving=False
            elif(t[i] in ImagesToPreImages):
                keepMoving=False
            else:
                preImagesToImages[s[i]]=t[i]
                ImagesToPreImages[t[i]]=s[i]
            i=i+1
        
        if(keepMoving==True):
            return True
        else:
            return False
                
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        listLength= len(strs)
    
        if(listLength==1):
            return strs[0]
        
        if ("" in strs):
            return ""
        
        commonPrefix=""
        smallestStrLength= len(strs[0])
        
        for i in range(1,listLength):
            if(len(strs[i])<smallestStrLength):
                smallestStrLength= len(strs[i])
        
        keepGoing=True
        i=0
        while(keepGoing==True and i<smallestStrLength):
        
            j=0
            testChar= strs[j][i]
            while(keepGoing==True and j<listLength):
                if(strs[j][i]!=testChar):
                    keepGoing=False

                j=j+1
            
            if(keepGoing==True):
                commonPrefix= commonPrefix + testChar
        
            i=i+1
        
        return commonPrefix


        
        
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        def checkOccurence(haystack,needle,haystackLength,needleLength,i):
            needleIterator=0
            haystackIterator=i
            while((needleIterator<needleLength)and(haystackIterator<haystackLength) and (haystack[haystackIterator]==needle[needleIterator])):
                needleIterator=needleIterator+1
                haystackIterator= haystackIterator+1
            
            if(needleIterator==needleLength):
                return True
            else:
                return False

        needleLength= len(needle)
        haystackLength = len(haystack)

        if(needleLength>haystackLength):
            return -1
        
        traversalLimit = haystackLength-needleLength+1
        found=False
        i=0

        while((i<traversalLimit) and (found==False)):
            if(needle[0]==haystack[i] and checkOccurence(haystack,needle,haystackLength,needleLength,i)==True):
                found=True
            i=i+1

        if(found==False):
            return -1
        else:
            return i-1
        



        
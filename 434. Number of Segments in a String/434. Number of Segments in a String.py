class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        size=len(s)
        i=0
        segments=0
        
        while(i<size):
            segmentEncountered=False
            while(i<size and s[i]==' '):
                i=i+1
            while(i<size and s[i]!=' '):
                segmentEncountered=True
                i=i+1
            if(segmentEncountered):
                segments=segments+1
        
        return segments
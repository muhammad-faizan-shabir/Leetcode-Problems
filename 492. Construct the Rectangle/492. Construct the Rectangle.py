class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """

        w = int(sqrt(area))
        l = int(area/w)

        while(l*w != area):
            w=w-1
            l= int(area/w)
        
        return [l,w]
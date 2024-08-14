class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        
        size=len(columnTitle)
        base=26
        weight=1
        columnNumber=0

        for i in range(size-1,-1,-1):
            columnNumber=columnNumber+(weight*(ord(columnTitle[i])-64))
            weight=weight*base

        return columnNumber
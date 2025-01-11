class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        
        columnTitle=""
        remaninder=None
        
        while(columnNumber>0):
            remainder= columnNumber%26
            columnNumber=columnNumber//26

            if(remainder==0):
                remainder=26
                columnNumber=columnNumber-1

            columnTitle = chr(remainder+64)+columnTitle

        return columnTitle
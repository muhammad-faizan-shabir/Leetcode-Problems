class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        row=[]

        for i in range(0,rowIndex+1):
            row.append((math.factorial(rowIndex)/((math.factorial(i))*(math.factorial(rowIndex-i)))))
        
        return row
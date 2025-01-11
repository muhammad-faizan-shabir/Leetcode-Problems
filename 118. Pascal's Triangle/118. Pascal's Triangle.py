class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        Triangle=[]

        for i in range(1,numRows+1):
            row=[0]*i
            leftPtr=0
            rightPtr=i-1
            row[leftPtr]=1
            row[rightPtr]=1
            leftPtr=leftPtr+1
            rightPtr=rightPtr-1
            if(i>1):
                prevRow=Triangle[i-2]
            
            while(leftPtr<=rightPtr):
                row[leftPtr]=prevRow[leftPtr-1]+prevRow[leftPtr]
                row[rightPtr]=row[leftPtr]
                leftPtr=leftPtr+1
                rightPtr=rightPtr-1
            
            Triangle.append(row)

        return Triangle



            

        
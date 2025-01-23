class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        baseSevenNum = ""
        positive = True
        
        if(num < 0):
            positive = False
            num = num * -1
        
        while(num >= 7):
            remainder = num%7
            num = num // 7
            baseSevenNum = str(remainder) + baseSevenNum
        
        baseSevenNum = str(num) + baseSevenNum
        
        if(positive == False):
            baseSevenNum = "-" + baseSevenNum

        return baseSevenNum
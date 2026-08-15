class Solution:
    def reverse(self, x: int) -> int:
        lowerBound = -2**31
        upperBound = (2**31) - 1
        negative = False
        
        if(x < 0):
            negative = True
            x = x * -1
        
        reverse = 0
        digit = x % 10
        reverse = reverse * 10 + digit
        x = x//10
        
        while(x > 0):
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x//10
        
        if(negative):
            reverse = reverse * -1
        
        if(reverse >= lowerBound and reverse <= upperBound):
            return reverse
        else:
            return 0
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        size= len(s)
        i = 0
        A_Count = 0
        
        while(i<size):
            if(s[i] == 'A'):
                A_Count=A_Count+1
        
                if(A_Count>1):
                    return False
        
            elif(s[i]=='L'):
                if(i+1<size and s[i+1]=='L' and i+2<size and s[i+2]=='L'):
                    return False
        
            i=i+1
        
        return True
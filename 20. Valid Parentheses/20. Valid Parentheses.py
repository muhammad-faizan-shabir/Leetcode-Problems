class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dictionary ={"(":")","{":"}","[":"]"}

        stack= []
        strLength= len(s)

        result = True
        i=0
        while(i<strLength and result==True):
            if(s[i] in dictionary):
                stack.append(dictionary[s[i]])
            elif(len(stack)==0 or stack.pop()!=s[i]):
                result= False
            i=i+1

        if(len(stack)!=0):
            result=False
        
        return result

        
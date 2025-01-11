class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        dictionary={"I":1,"II":2,"III":3,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        if s in dictionary:
            return dictionary[s]
        

        strLength= len(s)
        num=0
        i=0
        while(i<strLength):
            if((i<strLength-1) and (s[i]=="I") and ((s[i+1]=="V") or(s[i+1]=="X") )):
                num = num + (-(dictionary[s[i]])) + dictionary[s[i+1]]
                i=i+2
            elif((i<strLength-1) and (s[i]=="X") and ((s[i+1]=="L") or(s[i+1]=="C"))):
                num = num + (-(dictionary[s[i]])) + dictionary[s[i+1]]
                i=i+2
            elif((i<strLength-1) and (s[i]=="C") and ((s[i+1]=="D") or (s[i+1]=="M"))):
                num = num + (-(dictionary[s[i]])) + dictionary[s[i+1]]
                i=i+2
            else:
                num = num + dictionary[s[i]]
                i=i+1
        
        return num
           



        
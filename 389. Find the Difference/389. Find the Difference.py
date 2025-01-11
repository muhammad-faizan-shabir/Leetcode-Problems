class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result=0
        sizeOfS= len(s)
        sizeOfT= len(t)

        for i in range(0,sizeOfS):
            result= result ^ ord(s[i])

        for i in range(0,sizeOfT):
            result=result ^ ord(t[i])
        
        return chr(result)
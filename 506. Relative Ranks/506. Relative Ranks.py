class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        
        size=len(score)
        
        for i in range(0,size):
            score[i]= (score[i],i)
        
        score.sort(key=lambda x: x[0], reverse=True)

        ans=[]
        
        for i in range(0,size):
            ans.append(" ")

        if(size>0):
            ans[score[0][1]]="Gold Medal"
        
        if(size>1):
            ans[score[1][1]]="Silver Medal"
        
        if(size>2):
            ans[score[2][1]]="Bronze Medal"
        
        if(size>3):
            for i in range(3,size):
                ans[score[i][1]]=str(i+1)
        
        return ans
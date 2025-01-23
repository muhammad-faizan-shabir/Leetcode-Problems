class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        if(len(word)<2):
            return True
        
        if(word[0].islower()):
            return word.islower()
        else:
            return (word.isupper() or word[1::].islower())
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        dictionary={}
        
        for letter in s:
            dictionary[letter]=dictionary.get(letter,0) +1

        longestLength=0
        oddFrequencyExists=False
        
        for letter in dictionary:
            frequency= dictionary[letter]
            if(frequency%2==0):
                longestLength=longestLength +frequency
            else:
                oddFrequencyExists=True
                longestLength= longestLength+ frequency-1
        
        if(oddFrequencyExists):
            longestLength= longestLength+1

        return longestLength
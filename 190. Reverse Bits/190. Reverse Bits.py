class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        reverse=0
        bitCount=0

        while(n>0):
            bitCount=bitCount+1
            reverse=reverse<<1   # make space for next least significant bit
            lsb=n&1              # get the least significant bit
            reverse= reverse^lsb # put the least significant bit in the reverse number
            n=n>>1               # move to next least significant bit
        
        while(bitCount<32):      # add remaining 0s on the left side if any
            bitCount=bitCount+1
            reverse=reverse<<1

        return reverse
        
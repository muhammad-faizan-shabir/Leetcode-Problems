class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if(num==0):
            return "0"
        
        dictionary={0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"a",11:"b",12:"c",13:"d",14:"e",15:"f"}
        hexNumber=''
        bitCount=0
        
        while(bitCount<32):
            lsb1=num & 1
            num=num>>1
            lsb2=num & 1
            num=num>>1
            lsb3=num & 1
            num=num>>1
            lsb4=num & 1
            num=num>>1

            decimalNum= (8*lsb4)+ (4*lsb3)+ (2*lsb2)+ (1*lsb1)
            hexNumber= dictionary[decimalNum]+hexNumber
            bitCount=bitCount+4
        
        hexNumber=hexNumber.lstrip('0')

        return hexNumber
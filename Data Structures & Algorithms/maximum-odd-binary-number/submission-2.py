class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        counter = 0
        for i in s:
            if i=='1':
                counter+=1

        return (counter-1)*'1' + (len(s)-counter)*'0'+'1'
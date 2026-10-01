class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        # count how many 1
        counter = s.count('1')

        answer = ['0']*len(s)

        # add the one at the end
        answer[-1]='1'
        counter-=1

        # add in once
        i = 0 
        while counter>0:
            answer[i]='1'
            counter-=1
            i+=1
        
        return "".join(answer)


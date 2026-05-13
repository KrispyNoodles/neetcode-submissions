class Solution:
    def reverseBits(self, n: int) -> int:
        
        answer = 0

        # starting at the 31 because the 0th is a 0
        curr_bit = 31

        while n>0:
            
            # checking if it is a 1
            if n&1==1:
                
                # 2 pow
                answer+=2**(curr_bit)

            # shifting the n to the right by 1
            n=n>>1

            # decrease the curr_bit by 1
            curr_bit-=1

        return answer
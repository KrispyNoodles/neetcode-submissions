class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        carry = 0
        result = 0

        for i in range(32):
            
            # checking the value at each position
            # from right most to left
            a_bit = (a>>i)&1
            b_bit = (b>>i)&1

            if carry == 0:
                # checking for carry
                if a_bit==1 and b_bit==1:
                    carry = 1

                # either is 1
                elif a_bit==1 or b_bit==1:

                    # adding the bit to the correct position
                    # shifting the 1 to the left by i position
                    result = result | 1<<i
                    
            else:
                # checking for carry
                if a_bit==1 and b_bit==1:
                    carry = 1

                    result = result | 1<<i

                # either is 1
                elif a_bit==1 or b_bit==1:
                    carry = 1
                
                # both is 0
                else:
                    result = result | 1<<i

                    #reset carry 
                    carry=0
        
        if result > 0x7FFFFFFF:
            result = ~(result^0xFFFFFFFF)

        return result

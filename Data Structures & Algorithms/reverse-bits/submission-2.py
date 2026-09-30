class Solution:
    def reverseBits(self, n: int) -> int:
        
        bit_str = format(n, '032b')

        # flipping it
        bit_str = bit_str[::-1]
        
        print(bit_str)
        
        return int(bit_str,2)

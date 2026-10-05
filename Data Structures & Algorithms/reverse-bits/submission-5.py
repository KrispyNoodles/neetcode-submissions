class Solution:
    def reverseBits(self, n: int) -> int:
        
        # convert into string first then reverse
        bit_str = format(n,'032b')
        bit_str = bit_str[::-1]

        return int(bit_str,2)
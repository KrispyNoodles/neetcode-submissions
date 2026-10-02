class Solution:
    def reverseBits(self, n: int) -> int:
        
        # get the string
        string = format(n, '032b')

        string = string[::-1]

        answer = int(string,2)
        return answer
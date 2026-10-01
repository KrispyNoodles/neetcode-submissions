class Solution:
    def tribonacci(self, n: int) -> int:
        
        m = {}

        m[0] = 0
        m[1] = 1
        m[2] = 1

        if n<=2:
            return m[n]

        for i in range(3, n+1):

            m[i] = m[i-3] + m[i-2] + m[i-1] 

        return m[n]

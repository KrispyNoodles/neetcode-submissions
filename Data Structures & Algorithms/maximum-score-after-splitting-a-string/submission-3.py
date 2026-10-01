class Solution:
    def maxScore(self, s: str) -> int:
        
        answer = 0
        for i in range(1, len(s)):

            left = s[:i]
            left_sum = left.count('0')
            right = s[i:]
            right_sum = right.count('1')

            
            answer = max(answer, left_sum+right_sum)

        return answer
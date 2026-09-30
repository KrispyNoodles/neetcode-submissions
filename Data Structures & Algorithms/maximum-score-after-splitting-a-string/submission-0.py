class Solution:
    def maxScore(self, s: str) -> int:
        
        answer = 0

        for i in range(1, len(s)):

            left = s[:i]
            left_count = str(left).count('0') 

            right = s[i:]
            right_count = str(right).count('1') 

            answer = max(answer, left_count+right_count)

        return answer
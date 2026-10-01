class Solution:
    def scoreOfString(self, s: str) -> int:
        
        answer = 0

        for i in range(len(s)-1):

            answer += abs(int(ord(s[i])-int(ord(s[i+1]))))

        return answer
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        
        answer = 0

        # lets flip the str
        s = s[::-1]

        found = False

        i = 0

        while i< len(s):

            while i< len(s) and s[i].isalnum():
                answer+=1
                i+=1
                found = True

            if found == True:
                return answer

            i+=1
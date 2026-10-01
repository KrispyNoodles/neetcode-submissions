class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        

        i = 0
        answer = []

        while i<len(word1) and i<len(word2):
            answer.append(word1[i])
            answer.append(word2[i])
            i+=1


        # checking which counter never finish
        answer.append(word1[i:])
        answer.append(word2[i:])
        
        return "".join(answer)
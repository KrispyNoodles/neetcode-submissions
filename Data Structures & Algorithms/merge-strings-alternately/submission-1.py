class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        answer = ""
        
        # choose the longer word
        if len(word1)>=len(word2):

            for i in range(len(word2)):
                answer+=word1[i]
                answer+=word2[i]

            # if the word is longer than the current index then continue adding
            if i+1<len(word1):
                # add the end
                answer+=word1[i+1:]

        else:
            for i in range(len(word1)):
                answer+=word1[i]
                answer+=word2[i]
            
            if i+1<len(word2):
                # add the end
                answer+=word2[i+1:]

        return answer
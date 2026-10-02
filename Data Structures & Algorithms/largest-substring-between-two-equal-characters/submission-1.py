class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        firsIndx = {}
        lastIndx = {}

        for index, value in enumerate(s):
            
            if value not in firsIndx:
                firsIndx[value]=index
            else:
                lastIndx[value]=index

        # now find the biggest
        answer = -1
        
        for i in firsIndx:
            if i in lastIndx:
                answer = max(answer, lastIndx[i]-firsIndx[i]-1)

        return answer
            
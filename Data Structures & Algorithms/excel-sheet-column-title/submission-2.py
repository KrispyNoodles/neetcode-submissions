class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        

        answer = []

        # find the differnece
        while columnNumber>0:

            # because it is 0-index but ord(A) is 1 index
            columnNumber-=1

            # remmainer
            remmainder = columnNumber%26

            # trying to find that value is simi
            character = chr(ord('A')+remmainder)
            answer.append(character)

            columnNumber = columnNumber//26

        answer = "".join(answer)

        return answer[::-1]



            
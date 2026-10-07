class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        alpha_dict = {1:'A', 2: 'B', 3: 'C', 4:'D', 5: 'E', 6:'F', 7: 'G',
        8:'H', 9: 'I', 10:'J', 11: 'K', 12:'L', 13: 'M', 14:'N', 15: 'O',
        16: 'P', 17: 'Q', 18: 'R', 19:'S', 20: 'T', 21:'U', 22: 'V',
        23: 'W', 24: 'X', 25: 'Y', 26:'Z'
        }
        
        answer = []
        # get the value of the aplhabet
        # 26 alphabets
        while columnNumber>0:

            # because the alpha dict is a 1-index
            columnNumber-=1

            # how many remmainder I get is the second alphabet
            remmainder = columnNumber%26

            # how many times I can divide columnNumber by
            columnNumber = columnNumber//26

            answer.append(alpha_dict[remmainder+1])
        
        return "".join(answer)[::-1]
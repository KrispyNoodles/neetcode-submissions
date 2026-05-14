class Solution:
    def reverse(self, x: int) -> int:

        answer = []
        ans_pos = 1 
        add_negative = False
        MAX = 2**31- 1
        MIN = -(2**31)

        if x<10 and x>=0:
            return x
        
        # checking if x is negative
        if x<0:
            add_negative = True
            x = abs(x)

        while x>0:
            
            # extracts the last digit
            digit = x%10
            answer.append(str(digit))

            # move by the 10'th position
            x = x//10

        if add_negative:
            answer = -int("".join(answer))

        else: 
            answer = int("".join(answer))

        # returnining answer
        if MIN<answer<MAX:
            return answer
        else:
            return 0
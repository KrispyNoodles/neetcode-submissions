class Solution:
    def countBits(self, n: int) -> List[int]:
        
        answer = []

        for number in range(0,n+1):

            counter=0

            while number>0:

                if number&1==1:
                    counter+=1

                # shift n by right by 1
                number = number>>1

            answer.append(counter)

        return answer
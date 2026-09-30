class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        
        answer = 0

        # doods in the queue
        for i in range(len(tickets)):

            # if the doods in front of k, they def will need to buy their tickets first, including k himself
            if i<=k:
                # but only take the min
                answer+=min(tickets[i], tickets[k])

            else:
                # else take the guy on the right of the tickets being bought -1
                # since at the momment k is bought the answer is returned
                answer+=(min(tickets[i], tickets[k]-1))

        return answer
            
            
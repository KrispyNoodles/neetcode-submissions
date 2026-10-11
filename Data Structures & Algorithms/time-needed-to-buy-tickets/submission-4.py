class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        answer = 0

        for i in range(len(tickets)):

            if i<=k:
                answer+=min(tickets[k], tickets[i])
            else:
                answer+=min(tickets[k]-1, tickets[i])
        
        return answer
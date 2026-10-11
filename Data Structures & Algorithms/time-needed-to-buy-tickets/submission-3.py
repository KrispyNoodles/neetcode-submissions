class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        answer = 0

        # all the dudes on the left def have to buy
        bought = tickets[0:k+1]

        # all the dudes will be buying as much as the person at kth
        for ticket in bought:
            answer+=min(tickets[k], ticket)

        before_bought = tickets[k+1:]

        print(bought)
        print(before_bought)

        for ticket in before_bought:
            # whichever that is cheaper
            answer+=min(tickets[k]-1, ticket)

        return answer
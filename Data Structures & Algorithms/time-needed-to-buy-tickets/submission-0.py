class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        # every one second the person has a value that minuses 1
        pointer = 0
        counter = 0

        while tickets:
            
            # if pointer reaches len(tickets), change to the last person of the queue
            if pointer == len(tickets):
                pointer = 0
            
            # check if it is zero, if it is then move the pointer and skip the increment of counter
            if tickets[pointer]==0:

                pointer+=1

                # skip so that it does not minus the current ticket
                continue
            
            # at each point the person in queue-1
            tickets[pointer]-=1

            # counter
            counter+=1

            # did the person that just bought the ticket became 0
            if pointer == k and tickets[pointer]==0:
                return counter

            pointer+=1
            
from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        # two dicts
        outgoing_peeps = defaultdict(int)
        incoming_peeps = defaultdict(int)

        for t in trust:
            outgoing_peeps[t[0]] +=1
            incoming_peeps[t[1]] +=1
        
        for person in range(1,n+1):

            # person found
            if outgoing_peeps[person]==0 and incoming_peeps[person]==n-1:
                return person
        
        return -1
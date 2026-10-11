class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        m = {}

        # creating a default for all
        for i in range(n):
            m[i+1] = []
        
        # creating a set to keep track who trusted anyone before
        trust_people = set()
        
        # now go thrpugh all the trust
        for t in trust:
            left_t  = t[0]
            right_t = t[1]

            trust_people.add(left_t)

            # if the right_t has not been added in before add it in
            if left_t not in m[right_t]:
                m[right_t].append(left_t)
            
            # cant exit early because cant know for sure it will trust someone else later

        # go through all the values
        for key, value in m.items():
            if len(value) == n-1 and key not in trust_people:
                return key

        # it does not fulfil th condition
        return -1


from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        m = defaultdict(int)

        for i in nums:
            m[i]+=1
        
        m = sorted(m.items(), key=lambda x: x[1], reverse=True)
        answer = []

        for value, counter in m:
            answer.append(value)

        return answer[:k]

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        m = {}

        # sort here first
        nums.sort(reverse=True)

        for i in nums:
            if i not in m:
                m[i]=1
            else:
                m[i]+=1
            
        m = sorted(m.items(), key=lambda x:x[1])

        answer = []

        for value, count in m:

            for _ in range(count):
                answer.append(value)

        return answer
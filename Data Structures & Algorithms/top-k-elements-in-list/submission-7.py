class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # creating a dict
        d = {}

        for number in nums:
            if number in d:
                d[number]+=1
            else:
                d[number]=1
        
        # doing a sort based off the second value
        answer = sorted(d.items(), key=lambda x: x[1], reverse=True)

        counter = 0
        final_ans = []

        for val, count in answer:

            if counter<k:
                final_ans.append(val)
                counter+=1

            else:
                return final_ans
        return final_ans

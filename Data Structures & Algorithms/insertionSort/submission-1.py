# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:

        if not pairs:
            return []
        
        final_ans = []

        # refenece to the og list instead of sttoring its pointer
        final_ans.append(pairs[:])

        for index in range(1, len(pairs)):

            # first index 
            j = index-1

            # as long as j is not 0
            # and... the value is more than the current value
            while j>=0 and pairs[j+1].key < pairs[j].key:
                
                # do the swaip
                temp_val = pairs[j+1]
                pairs[j+1] = pairs[j]
                pairs[j] = temp_val

                # decement
                j -= 1
            
            final_ans.append(pairs[:])

        return final_ans

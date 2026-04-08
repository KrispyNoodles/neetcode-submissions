class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        new_arr = []
        
        length_arr = len(arr)

        for index, value in enumerate(arr):

            if index != length_arr-1:
                # create a temp array to find the largest val
                temp_arr = arr[index+1:length_arr]
                new_arr.append(max(temp_arr))

            else:
                new_arr.append(-1)
            
        return new_arr
# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        s = 0
        e = len(pairs)-1
        
        self.quickSort_function(pairs, s, e)

        return pairs
    
    def quickSort_function(self, arr, s, e):

        # this is to check for cases where it is just a single elemtn
        # it is the same means it is the same element
        # and also catches the segments where it is empty
        if s>=e:
            return arr
            
        # the pivot value is the value at the end of the array
        pivot = arr[e].key
        left = s

        for i in range(s, e):
            
            if pivot > arr[i].key:

                # do the swap
                arr[i], arr[left] = arr[left], arr[i] 

                # increment s
                left += 1
        
        # after evertyhing swap the last i with the pivot value
        arr[left], arr[e] = arr[e], arr[left]

        # running quicksort on left and right after the pivot has been placed
        self.quickSort_function(arr, s, left-1)
        self.quickSort_function(arr, left+1, e)

        return arr
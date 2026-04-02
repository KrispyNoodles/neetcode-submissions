from typing import List

# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        self.own_mergeSort(pairs, 0, len(pairs)-1)

        return pairs

    # Merge Sort
    def own_mergeSort(self,arr, s, e):

        # this is the last layer with only 1 element
        if e - s + 1 <= 1:
            return arr
        
        # the middle index
        m = (e + s) // 2

        # sort the left half
        self.own_mergeSort(arr, s, m)

        # sort the right half
        self.own_mergeSort(arr, m + 1, e)

        # merge both sorted halfs together
        self.merge(arr, s, m, e)
        
        return arr


    def merge(self,arr, s, m, e):

        # create temp arrays
        # [start_index: end_index], slicing does not invlude the end_indedx whihch is why it needs a +1
        left = arr[s: m + 1]
        right = arr[m + 1: e + 1]

        # while i and j are lesser than the len of the arrays
        i = 0
        j = 0

        # index of array being inserted to
        k = s

        while i < len(left) and j <len(right):

            if left[i].key <= right[j].key:

                # place the smaller value into the array
                arr[k] = left[i]

                # icnrement i since it was used
                i += 1

            else:
                arr[k] = right[j]
                j += 1

            # increment k
            k += 1

        # add in the end when either do not have any more values
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
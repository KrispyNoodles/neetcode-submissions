import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
    heapq.heapify(arr)
    return arr[0]
    pass


def get_min_4_elements(arr: List[int]) -> List[int]:

    heapq.heapify(arr)

    answer = heapq.nsmallest(4, arr)
    return answer
    pass


def get_min_2_elements(arr: List[int]) -> List[int]:

    heapq.heapify(arr)

    answer = heapq.nsmallest(2, arr)
    return answer[::-1]
    pass


# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))


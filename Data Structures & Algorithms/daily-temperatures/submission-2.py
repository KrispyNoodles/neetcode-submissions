from typing import List

# my soln
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        # how many days before encountering a warmer day

        # monotonic decreasing stack
        # because the value at the top of stack is by right supposedly the smallest

        answer = [0]*len(temperatures)

        # create 0 array
        index_stack = []

        for index in range(len(temperatures)):

            # current value is larger than the one in the stack
            while index_stack and temperatures[index] > temperatures[index_stack[-1]]:

                # pop the value in the stack
                pop_index = index_stack.pop()

                # to find the days is just the current index-pop_index
                answer[pop_index] = index-pop_index

            index_stack.append(index)
        
        return answer
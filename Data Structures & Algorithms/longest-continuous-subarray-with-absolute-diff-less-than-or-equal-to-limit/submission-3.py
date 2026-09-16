class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        # creating two monotonic stack one decreasing and one increasing
        min_q = deque()
        max_q = deque()
        l = 0
        answer = 0

        for r in range(len(nums)):
            
            # while the stack is not emtpy and the new value is smaller than the stack
            while min_q and nums[r]<min_q[-1]:
                min_q.pop()
            
            while max_q and nums[r]>max_q[-1]:
                max_q.pop()

            min_q.append(nums[r])
            max_q.append(nums[r])

            while max_q[0]-min_q[0]>limit:
                if nums[l]==max_q[0]:
                    max_q.popleft()
                if nums[l]==min_q[0]:
                    min_q.popleft()
                l+=1
            answer = max(answer, r-l+1)

        return answer
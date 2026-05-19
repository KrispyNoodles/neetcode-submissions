class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # bucket sort

        bucket_s = {}

        for i in nums:
            if i not in bucket_s:
                bucket_s[i] = 1

            else:
                bucket_s[i]+=1

        answer = []

        # sort the bucket
        bucket_s = sorted(bucket_s.items(), key=lambda x: x[0])
        for key, value in bucket_s:
            for _ in range(value):
                answer.append(key)
                
        for a in range(len(nums)):
            nums[a]=answer[a]
        
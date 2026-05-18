class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # creating a set
        answer = set(nums)

        len_answer = len(answer)
        answer = list(answer)
        answer.sort()

        nums[:len_answer] = answer

        return len_answer
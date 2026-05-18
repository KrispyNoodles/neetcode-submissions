class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # creating a set
        answer = sorted(set(nums))

        len_answer = len(answer)

        nums[:len_answer] = list(answer)

        return len_answer
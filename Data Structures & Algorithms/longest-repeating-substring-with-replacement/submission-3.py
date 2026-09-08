class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # creating a dict
        d = {}

        # checking left and the answer
        left = 0
        answer = 0

        # variable to track the most number of occurence, 
        # because this is only updated when we have a new potential answer
        # if not we can just take the last updated one
        most_char = 0
        
        for right in range(len(s)):

            # adding the value into the map
            if s[right] in d:
                d[s[right]]+=1
            else:
                d[s[right]]=1

            # updating max w.r.t the new added elemtn
            most_char = max(most_char, d[s[right]])

            # checking when the current segment is valid and invalid
            # invalid
            while right-left+1-(most_char)>k:
                
                # reduce the count of the dudes in the left from the dict
                d[s[left]]-=1
                left+=1
   
            # update answer
            answer = max(answer, right-left+1)

        return answer
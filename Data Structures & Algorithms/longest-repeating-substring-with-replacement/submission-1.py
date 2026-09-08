class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # creating a dict
        d = {}

        left = 0
        answer = 0

        for right in range(len(s)):

            # adding the value into the map
            if s[right] in d:
                d[s[right]]+=1
            else:
                d[s[right]]=1

            # retrieving the value that counts the most amount of char
            most_char = max(d.values())

            # checking when the current segment is valid and invalid
            # invalid
            while right-left+1-(most_char)>k:
                
                # reduce the count of the dudes in the left from the dict
                d[s[left]]-=1
                left+=1
   
            # update answer
            answer = max(answer, right-left+1)

        return answer
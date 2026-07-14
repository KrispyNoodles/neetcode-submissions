class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # minimm is 1
        answer = 1

        

        i = 0

        # check if i is within
        while i < len(s):
  

            # declaration of a new visited set
            visited = set()
            counter = 1
            a = i

            # checking that a is within the range and not in visited
            while a<len(s) and s[a] not in visited:
                # add it into the set
                visited.add(s[a])

                # increment the counter and update the answer
                counter +=1
                answer = max(counter, answer)

                # increment a
                a+=1

            i+=1
            # if exit then resets
        
        return answer-1

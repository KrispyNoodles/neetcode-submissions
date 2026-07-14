class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charS = set()
        left = 0

        answer = 0

        # right will go through every single character to the end
        for right in range(len(s)):
            
            # if we visit a dude thats already in the set, 

            # then we pop all the dueds till we reach the dude that was inside the set
            # and add the new dude in
            while s[right] in charS:

                # remove the right
                charS.remove(s[left])

                # then move the left
                left+=1
            
            # else add the character in
            charS.add(s[right])

            # update the answer everytime we add a new duded in
            answer = max(answer, right-left+1)

        return answer
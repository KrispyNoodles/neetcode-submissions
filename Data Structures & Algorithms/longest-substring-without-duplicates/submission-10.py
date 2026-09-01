class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        seen = set()
        answer = 0

        # left is the one moving?
        for right in range(len(s)):
            
            if s[right] not in seen:

                # add the left inside
                seen.add(s[right])

                # update the seen set
                answer = max(answer, right-left+1)

            else:
                # if the new right is still inside keep removing all the elements from left inside until it is remove
                while s[right] in seen:

                    # remove the left and increment it
                    seen.remove(s[left])
                    left+=1

                # ad in the s[right] after
                seen.add(s[right])
        
        return answer
            
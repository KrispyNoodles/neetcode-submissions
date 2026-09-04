class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        answer = 0

        left = 0
        current_set = set()

        for right in range(len(s)):

            # skip the situation where right =0
            if right==0:
                answer = 1

                current_set.add(s[right])
                continue

            while s[right] in current_set:
                
                # remove it from the set
                current_set.remove(s[left])

                left+=1

            # recal answer
            answer = max(answer, right-left+1)

            # add in right
            current_set.add(s[right])
        
        return answer

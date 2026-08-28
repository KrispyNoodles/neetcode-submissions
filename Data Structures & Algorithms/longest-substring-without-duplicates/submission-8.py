class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        visited = set()
        answer = 0

        for right in range(len(s)):

            while s[right] in visited:
                visited.remove(s[left])
                left+=1
            
            # add the right into visit
            visited.add(s[right])

            # update the answer
            answer = max(answer, len(visited))


        return answer

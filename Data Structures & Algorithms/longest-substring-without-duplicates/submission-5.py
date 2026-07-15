class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # creating 2 pointers
        left = 0
        visited = set()
        answer = 0
        
        for right in range(len(s)):

            # if dude inside visited
            while s[right] in visited:

                # remove it from the left pointer from the set
                visited.remove(s[left])
                left+=1

            # add the right into the visited
            visited.add(s[right])

            # update the answer everytiem it is added
            answer = max(answer, len(visited))


        
        return answer


        
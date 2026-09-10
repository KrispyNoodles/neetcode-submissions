class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        # creatinga dict that counts the frequency of items
        temp_d = {}

        left = 0

        answer = 0

        for right in range(len(s)):

            # add right into the dict
            if s[right] not in temp_d:
                temp_d[s[right]]=1
            else:
                temp_d[s[right]]+=1

            # checking if it is a valid answer
            while right-left-max(temp_d.values())+1>k:
                # remove it from the dict
                temp_d[s[left]]-=1

                # and shift left
                left+=1
            
            answer = max(answer, right-left+1)
        
        return answer
# Memoization
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # creating a 2d matrix containing of the values containign the length
        # r is index 1 of text 1 and c is index 2 of text2

        # creating the cache
        cacheMatrix = [[-1]*len(text2) for _ in range(len(text1))]
        
        def helperFn(index_1, index_2, cache):
            

            # if the index is further than the len, return 0
            if index_1==len(text1) or index_2==len(text2):
                return 0 
            
            # checking if it is inside
            if cache[index_1][index_2]!=-1:
                return cache[index_1][index_2]

            char_1, char_2 = text1[index_1], text2[index_2]

            # in a situation where both characters matches, then move both text
            if char_1==char_2:
                cache[index_1][index_2] = 1+helperFn(index_1+1, index_2+1, cacheMatrix)
                return cache[index_1][index_2]

            # if both characters are different, I have a choice to either move text1 or text2
            elif char_1!=char_2:
                cache[index_1][index_2] = max(helperFn(index_1, index_2+1, cacheMatrix), helperFn(index_1+1, index_2, cacheMatrix))
                return cache[index_1][index_2]

        return helperFn(0,0, cacheMatrix)
        
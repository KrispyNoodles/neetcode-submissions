# Dynamic Programming/ Bottom Up Programming

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # creating the cache
        # matrix has to be bigger so that the checks for the diagonal or the left and right wont return the out of index error
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]    

        # i is row and j is col
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):

                if text1[i] == text2[j]:

                    # add the guys on the diagnoal
                    # and it is moving up diagnoally left/up
                    dp[i][j] = 1 + dp[i+1][j+1]

                # check if either go down left or right
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        
        # answer will be the top left
        return dp[0][0]

# time complexity of O(n*m)
# space complexity of O(n*m)
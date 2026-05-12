# Memoisattion
class Solution:
    def climbStairs(self, n: int) -> int:
        
        def helperFn(n, cache):
            # if you are at stair 1, you have 1 method only
            if n==1:
                return 1
            
            # if you are at stair 2, you have 2 methods 1+1 and 2
            if n==2:
                return 2
            
            # checkinf if n has been solved before
            if n in cache:
                return cache[n]

            cache[n] = helperFn(n-1, cache) + helperFn(n-2, cache) 
        
            return cache[n]
    
        return helperFn(n, {})

# time complexity O(n)
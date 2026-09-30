class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if flowerbed==[0] and n==1:
            return True
        
        for i in range(0, len(flowerbed)-1):

            # if i is the first case or the last we can plant
            if i==0  and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                n-=1
                flowerbed[i]=1

                # skip everything after
                continue
            
            # checking if the flower beside is empty
            if flowerbed[i] == 0:
                # check if the left is empty
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    # plant the flower and reduce count
                    n-=1
                    flowerbed[i]=1

            # if i is the last case
            if i==len(flowerbed)-2  and flowerbed[len(flowerbed)-2] == 0 and flowerbed[len(flowerbed)-1] == 0:
                n-=1
                flowerbed[i]=1

                # skip everything after
                continue
            
        if n<=0:
            return True

        else:
            return False
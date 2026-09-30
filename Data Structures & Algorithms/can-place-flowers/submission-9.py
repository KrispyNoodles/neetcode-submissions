class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        for i in range(len(flowerbed)):

            # checking if left empty or if it is the first elemnt
            left_empty = i == 0 or flowerbed[i - 1] == 0

            # checking if it is right emepty or the last eleemtn
            right_empty = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0

            # checking if the current location is actually emtpy to put and both sides are empty
            if flowerbed[i] == 0 and left_empty and right_empty:
                flowerbed[i] = 1
                n -= 1

                # early cancellation
                if n <= 0:
                    return True

        # after everything if there are pots left
        return n <= 0
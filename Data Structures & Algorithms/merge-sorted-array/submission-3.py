class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # m is always longer than n

        length = m+n-1

        # first we add in values into n
        while m>0 and n>0:
            
            # trying to see which is bigger to add to the end
            if nums1[m-1] >= nums2[n-1]:
                nums1[length] = nums1[m-1] 
                
                # decrease m
                m-=1

            else:
                nums1[length] = nums2[n-1]

                # decrease n
                n-=1

            # move the length back by 1
            length-=1

        # add it to the front?
        while n != 0:
            nums1[length] = nums2[n-1]
            n-=1
            length-=1
        


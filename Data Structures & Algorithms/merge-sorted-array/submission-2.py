class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # having 3 pointer
        write = m+n-1
        
        
        # work down from len to 0
        while m>0 and n>0:

            # comparison to know which should be added to the end
            if nums1[m-1] >= nums2[n-1]:

                # putting the bigger number at the end
                nums1[write] = nums1[m-1]
                m-=1
                write-=1

            else:
                nums1[write] = nums2[n-1]

                # decrease both n only
                n-=1
                write-=1

        # copy the remaninig elements in
        while n>0:
            nums1[write] = nums2[n-1]
            n-=1
            write-=1

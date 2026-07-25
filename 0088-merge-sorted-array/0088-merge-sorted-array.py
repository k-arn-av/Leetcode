class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        read_index=m-1
        write_index=m+n-1
        reference_index=n-1

        while reference_index>=0:
            if read_index>=0 and nums1[read_index]>nums2[reference_index]:
                nums1[write_index]=nums1[read_index]
                read_index-=1
            else:
                nums1[write_index]=nums2[reference_index]
                reference_index-=1
            write_index-=1



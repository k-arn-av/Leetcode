class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index_to_swap=len(nums)-k
        for i in range(index_to_swap,len(nums)):
            nums.insert(0,nums.pop())

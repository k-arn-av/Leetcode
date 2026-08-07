class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=len(nums)-1

        while i>=1 and nums[i]<=nums[i-1]:
            i-=1
        pivot=i-1
        
        if pivot>=0:
            j=len(nums)-1
            while j>=0 and nums[j]<=nums[pivot]:
                j-=1

            nums[pivot],nums[j]=nums[j],nums[pivot]
        
        left=i
        right=len(nums)-1

        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1



        
        
        

        



        
        





        
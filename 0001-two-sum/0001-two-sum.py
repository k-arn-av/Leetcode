class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        save={}
        for index,num1 in enumerate(nums):
            compliment=target-num1
            if compliment in save:
                return (save[compliment],index)
            else:
                save[num1]=index
        

        
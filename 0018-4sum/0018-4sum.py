class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        res=[]


        if len(nums)==4:
            if sum(nums)==target:
                return [nums]
            return []

        elif len(nums)<4:
            return []

        for first in range(len(nums)):
            if first>0 and nums[first]==nums[first-1]:
                continue

            for second in range(first+1,len(nums)):
                left=second+1
                right=len(nums)-1
                
                if second> first+1 and nums[second]==nums[second-1]:
                    continue

               
                while left<right:
                    if nums[left]+nums[right]== target-nums[first]-nums[second]:
                        res.append([nums[left],nums[right], nums[first], nums[second]])

                        while(left<right and nums[left]==nums[left+1]):
                            left+=1
                        while (left < right and nums[right] == nums[right - 1]):
                            right-=1
                        left+=1
                        right-=1

                    elif nums[left]+nums[right]>target-nums[first]-nums[second]:
                        right-=1
                    else:
                        left+=1

                  
                    
        return res





        




        
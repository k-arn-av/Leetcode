class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #threesum 
        nums.sort()
        storelist=[]

        for i in range(len(nums)):

            if i>0 and nums[i]==nums[i-1]:
                continue

            left=i+1
            right=len(nums)-1
            while(left<right):
                twosum= nums[left]+nums[right]

                if twosum<-nums[i]:
                    left+=1
                elif twosum>-nums[i]:
                    right-=1
                else:
                    storelist.append([nums[i],nums[left],nums[right]])

                    while(left<right and nums[left]==nums[left+1]):
                        left+=1
                    while (left < right and nums[right] == nums[right - 1]):
                        right-=1
                    left+=1
                    right-=1
                    
        return storelist


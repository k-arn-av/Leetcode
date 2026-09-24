class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        left=0
        total=0
        maxmean=float("-inf")
        for right in range(len(nums)):
            total+=nums[right]

            if right-left+1==k:
                mean=(total/k)
                maxmean=max(mean,maxmean)
                total-=nums[left]

                left+=1

        return maxmean



        
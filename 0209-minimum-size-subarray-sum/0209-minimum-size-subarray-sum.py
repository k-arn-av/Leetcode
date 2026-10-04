class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        msum=0
        left=0
        minlen=float("inf")
        for right in range(len(nums)):
            msum+=nums[right]

            while msum>=target:
                minlen=min(minlen, right-left+1)
                msum-=nums[left]
                left+=1
        if minlen==float("inf"):
            return 0
        return minlen

        
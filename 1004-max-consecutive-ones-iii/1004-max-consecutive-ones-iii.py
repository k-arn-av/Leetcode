class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left=0
        maxlen=0
        hsh={}
        for right in range(len(nums)):
            hsh[nums[right]]=hsh.get(nums[right],0)+1

            while hsh.get(0, 0)>k:
                hsh[nums[left]]=hsh.get(nums[left],0)-1
                if hsh[nums[left]]<=0:
                    del hsh[nums[left]]

                left+=1

            maxlen=max(maxlen, right-left+1)
        return maxlen

        



            
            
                

        
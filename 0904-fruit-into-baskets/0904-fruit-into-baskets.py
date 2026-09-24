class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        #two windows for the given array allowed
        left=0
        basket=2
        maxlen=0
        hsh={}
        for right in range(len(fruits)):

            hsh[fruits[right]]=hsh.get(fruits[right],0)+1

            while len(hsh)>2:
                hsh[fruits[left]]=hsh.get(fruits[left],0)-1
                if hsh[fruits[left]]==0:
                    del hsh[fruits[left]]
                left+=1

            maxlen=max(maxlen,right-left+1)
        return maxlen



class Solution:
    def maxArea(self, height: list[int]) -> int:
        #two pointers converge
        
        left=0
        right=len(height)-1

        max_area=0

        while (left<right):

            difference=right-left
            minimum=min(height[left],height[right])
            current_area= difference* minimum
            max_area=max(max_area,current_area)

            if minimum==height[left]:
                left+=1
            else:
                right-=1
        return max_area

                



                


        
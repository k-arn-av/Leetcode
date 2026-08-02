class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            result=0
            updated_n=n
            while updated_n>0:
                digit=updated_n%10
                result+=digit**2
                updated_n=updated_n//10
            return result
        
        if n==1:
            return True
        slow=n
        fast=get_next(n)
        while fast!=1 and slow!=fast:
            slow=get_next(slow)
            fast=get_next(get_next(fast))
        return fast==1
            
    
    
    




    

            
        




        
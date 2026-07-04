class Solution:
    def canJump(self, a: List[int]) -> bool:
        n = len(a)
        if n == 0:
            return False

        if n == 1:
            return True

        
        gas = a[0]
        if gas <= 0:
            return False
            
        for i in range(1, n):

            gas -=1 
            gas = max(gas, a[i])

            if gas <=0 and i !=n-1:
                return False

        if gas>=0:
            return True
        else:
            return False

        


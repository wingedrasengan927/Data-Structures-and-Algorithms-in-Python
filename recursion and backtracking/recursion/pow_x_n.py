class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            return 1/self.myPow(x, -n)
        
        if n % 2 == 0:
            return self.myPow(x*x, n//2)
        else:
            return x*self.myPow(x, n-1)
            
    def myPowMemo(self, x, n):
        memo = {}
        def myPowHelper(x, n):
            # base case
            if n == 0:
                return 1
            elif n == 1:
                return x
            
            elif n < 0:
                x = (1/x)
                n = abs(n)
                
            # memoization
            if (x, n) in memo:
                return memo[(x, n)]
            
            if n % 2 == 0:
                memo[(x, n)] = myPowHelper(x, n//2) * myPowHelper(x, n//2)
            else:
                memo[(x, n)] = myPowHelper(x, n//2) * myPowHelper(x, n - n//2)
            return memo[(x, n)]
        return myPowHelper(x, n)
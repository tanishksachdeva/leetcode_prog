# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
# Example 4:

# Input: x = 0
# Output: 0

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0 
        sign = 1
        if x < 0:
            x*=-1
            sign = -1
            
            
        while(x > 0):  
            r = x %10    
            rev = (rev *10) + r    
            x = x //10
            
        if rev > 2**31-1 or rev < -2**31:
            return 0

            
        return sign*rev
    
    def reverse_string_solution(self, x: int) -> int:
        if x < 0:
            x *= -1
            x = int(str(x)[::-1]) * -1
        else:
             x = int(str(x)[::-1])
                
        if x > 2**31 -1 or x < (2**31 -1) * -1:
            return 0
        
        return x
#Definition 
"""
    Given a 32-bit signed integer, reverse digits of an integer.

    Example 1:

    Input: 123
    Output: 321
    Example 2:

    Input: -123
    Output: -321
    Example 3:

    Input: 120
    Output: 21
    Note:
    Assume we are dealing with an environment which could only store integers 
    within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose 
    of this problem, assume that your function returns 0 when the reversed 
    integer overflows.
"""

class Solution:


    def reverse(self, x):
        negFlag = 1
        if x < 0:
            negFlag = -1
            strx = str(x)[1:]
        else:
            strx = str(x)

        x = int(strx[::-1])
        
        return 0 if x > pow(2, 31) else x * negFlag

test = Solution()

print(test.reverse(123))
print(test.reverse(-123))
print(test.reverse(120))
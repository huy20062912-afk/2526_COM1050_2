# Exercise 69: Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        L, R = 1, x
        while L <= R:
            M = (L + R) // 2
            M_squared = M * M
            if M_squared == x:
                return M
            elif M_squared < x:
                L = M + 1
            else:
                R = M - 1
        return R
    
# This is my first implementation of binary search
# Binary search is a powerful algorithm for finding an item from a sorted list of items.
# It works by repeatedly dividing in half the portion of the list that could contain the item,
# until you've narrowed down the possible locations to just one.
# In this case, we are using binary search to find the integer square root of x.
# The integer square root of a non-negative integer x is the greatest integer y such that y*y <= x.
# We initialize our search range with L = 1 and R = x.
# We then enter a loop that continues as long as L is less than or equal to R.
# In each iteration, we calculate the midpoint M of the current range.
# We then compute M_squared = M * M to avoid recalculating it multiple times.
# If M_squared is equal to x, we have found the exact square root and return M
# If M_squared is less than x, it means the square root must be larger than M,
# so we adjust our search range to the right half by setting L = M + 1
# If M_squared is greater than x, it means the square root must be smaller than M,
# so we adjust our search range to the left half by setting R = M - 1
# When the loop ends, L will be greater than R, and R will be the largest integer
# such that R*R <= x, which is the integer square root we want to return
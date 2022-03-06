# Given a positive integer n, calculate the following sum:

# n + n/2 + n/4 + n/8 + ...
# All elements of the sum are the results of integer division.

# Example
# 25  =>  25 + 12 + 6 + 3 + 1 = 47

def halving_sum(n): 
    if n == 1:
        return n
    else:
        return halving_sum(n//2) +n
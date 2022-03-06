# Have a look at the following numbers.

#  n | score
# ---+-------
#  1 |  50
#  2 |  150
#  3 |  300
#  4 |  500
#  5 |  750
# Can you find a pattern in it? If so, then write a function getScore(n)/get_score(n)/GetScore(n) which returns the score for any positive number n.


def get_score(n):
    r=0
    for i in range(1,n+1):
        r += i*50
    return r    
        







def get_score(n):
    if n==1:
        return 50
    else:    
        return  get_score(n-1) + n*50
        
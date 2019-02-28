import time
import sys
n = int(sys.argv[1])
old = sys.getrecursionlimit()
sys.setrecursionlimit(1000000)
def good_fibonacci(n):
    if n <= 1:
        return (n,0)
    else:
        (a, b) = good_fibonacci(n-1)
        print a
        return (a+b, a)

def time_1(n):
    start = time.time()
    good_fibonacci(n)
    print '%f' % (time.time() - start) 

def linear_sum(S, n):
    """Return the sum of first n number of sequence S."""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]


S = [4, 3, 6, 2, 8]
if __name__ == '__main__':
    linear_sum(S, n)
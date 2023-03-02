def Calculator(n, p):
    if n < 0 or p < 0:
        raise ValueError("n and p should be non-negative")
        
    result = n ** p
    return result
    
myCalculator = Calculator  # remove the parentheses

T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator(n, p)  # call myCalculator with n and p as arguments
        print(ans)
    except Exception as e:
        print(e)
##Input from stdin is handled for you by the locked stub code in your editor. The first line contains an integer,T, the number of test cases. Each of the T subsequent lines describes a test case in 2 space-separated integers that denote n and p, respectively.
# This code seems not meeting the test cases, hence it's re-written in C++, refer NpowerP.cpp

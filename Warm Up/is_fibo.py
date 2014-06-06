# You are given an integer, N. Find out if the number is an element of fibonacci
# series.

# The first few elements of fibonacci series are 0,1,1,2,3,5,8,13.. A fibonacci
# series is one where every element is a sum of the previous two elements in the
# series. The first two elements are 0 and 1.

# Formally:

# fib0 = 0
# fib1 = 1
# fibn = fibn-1 + fibn-2 ^A n > 1

# Input Format
# The first line contains T, number of test cases.
# T lines follows. Each line contains an integer N.

# Output Format
# Display "IsFibo" (without quotes) if N is a fibonacci number and "IsNotFibo"
# (without quotes) if it is not a fibonacci number. The output for each test
# case should be displayed on a new line.

# 1 <= T <= 105
# 1 <= N <= 1010

# Sample Input

# 3
# 5
# 7
# 8
# Sample Output

# IsFibo
# IsNotFibo
# IsFibo

# Explanation
# 5 is a Fibonacci number given by fib5 = 3 + 2
# 7 is not a Fibonacci number
# 8 is a Fibonacci number given by fib6 = 5 + 3


values = [input() for _ in xrange(input())]
max_value = max(values)

a = 0
b = 1
fibo = [a, b]
while b <= max_value:
    c = a + b
    a = b
    b = c
    fibo.append(c)

for value in values:
    if value in fibo:
        print 'IsFibo'
    else:
        print 'IsNotFibo'

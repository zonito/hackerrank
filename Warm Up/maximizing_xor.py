# Given two integers: L and R,

# find the maximal values of A xor B ^A L <= A <= B <= R

# Input Format
# The input contains two lines, L is present in the first line.
# R in the second line.

# Constraints
# 1 <= L <= R <= 10^3

# Output Format
# The maximal value as mentioned in the problem statement.

# Sample Input
# 1
# 10

# Sample Output
# 15

# Explanation
# The maximum value can be obtained for A = 5 and B = 10,
# 1010 xor 0101 = 1111 hence 15.


def  maxXor( l,  r):
    xmax = 0
    for i in range(1, 11):
        factor = (pow(2, i) - 1)
        xor_r = factor ^ r
        xor_l = factor ^ l
        if xor_r <= r and xor_l >= l:
            xmax = max(xmax, factor)
    return xmax


_l = int(raw_input());

_r = int(raw_input());

res = maxXor(_l, _r);
print(res)

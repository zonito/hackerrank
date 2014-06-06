# Bill Gates is on one of his philanthropic journeys to a village in Utopia. He
# has N packets of candies and would like to distribute one packet to each of
# the K children in the village (each packet may contain different number of
# candies). To avoid any fighting among the children, he would like to pick K
# out of N packets, such that unfairness is minimized.

# Suppose the K packets have (x1, x2, x3,...,xk) candies in them, where xi denotes
# the number of candies in the ith packet, then we define unfairness as

# max(x1,x2,...,xk) - min(x1,x2,...,xk)

# where max denotes the highest value amongst the elements, and min denotes the
# least value amongst the elements. Can you figure out the minimum unfairness
# and print it?

# Input Format
# The first line contains an integer N.
# The second line contains an integer K. N lines follow. Each line contains an
# integer that denotes the candy in the ith packet.

# Output Format
# A single integer which will be the minimum unfairness.

# Constraints
# 1<=N<=105
# 1<=K<=N
# 0<= number of candies in any packet <=109

# Sample Input #00

# 7
# 3
# 10
# 100
# 300
# 200
# 1000
# 20
# 30
# Sample Output #00

# 20
# Explanation #00
# Here K = 3. We can choose packets that contain 10,20,30 candies. The
# unfairness is

# max(10,20,30) - min(10,20,30) = 30 - 10 = 20
# Sample Input #01

# 10
# 4
# 1
# 2
# 3
# 4
# 10
# 20
# 30
# 40
# 100
# 200
# Sample Output #01

# 3
# Explanation #01
# Here K = 4. We can choose the packets that contain 1,2,3,4 candies. The unfairness is

# max(1,2,3,4) - min(1,2,3,4) = 4 - 1 = 3

n = input()
k = input()
candies = [input() for _ in range(0,n)]
candies.sort()

## Write code here to compute the answer using (n, k, candies)
min_diff = min([candies[i + k - 1] - candies[i] for i in xrange(n - k + 1)])

print min_diff
# James got hold of a love letter that his friend Harry has written for his
# girlfriend. Being the prankster that James is, he decides to meddle with it.
# He changes all the words in the letter into palindromes. For any given string,
# he can only decrease the value of any one of the letters, for example, 'd'
# will become 'c', etc. This will count as one operation. (Also, he can decrease
# the value of letters only till he reaches 'a'. 'a' cannot be further reduced
# to 'z') Find the minimum number of operations he needs to carry out to convert
# a given string into a palindrome.


# Input Format
# The first line contains an integer T i.e. number of test cases.
# The next T lines will contain a string each.

# Output Format
# A single line containing number of minimum operations corresponding to each
# test case.

# Constraints
# 1 <= T <= 10
# 1 <= length of string <= 104

# Sample Input #00
# 3
# abc
# abcba
# abcd

# Sample Output #00
# 2
# 0
# 4

# Explanation
# For the first test case, abc -> abb -> aba.
# For the second test case, abcba is a palindromic string.
# For the third test case, abcd -> abcc -> abcb -> abca = abca -> abba.


import string

alpha_list = list(string.ascii_lowercase)

for _ in range(input()):
    word = raw_input()
    len_word = len(word)
    sum = 0
    for i in range(len_word / 2):
        last_char = word[len_word - i - 1]
        if word[i] != last_char:
            sum += abs(alpha_list.index(last_char) - alpha_list.index(word[i]))
    print sum

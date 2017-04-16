'''
Given a string, you need to reverse the order of characters in each word 
within a sentence while still reserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will 
not be any extra space in the string.

------------------

Spend time understanding the one liner solutions for this problem

1. return " ".join(map(lambda x: x[::-1], s.split()))
2. return ' '.join([i[::-1] for i in s.split()])
'''
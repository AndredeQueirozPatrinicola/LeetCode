'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        lst = []
        string = ""
        n = 0

        x_to_str = str(x)

        for i in x_to_str:
          lst.append(i)

        lst.reverse()

        conv = string.join(lst)

        if conv == x_to_str:
          return True
        else:
          return False

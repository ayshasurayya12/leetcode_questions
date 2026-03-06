# Given an integer num, return the number of digits in num that divide num.

# An integer val divides nums if nums % val == 0.

class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0

        for digit in str(num):
            digit = int(digit)
            if num % digit == 0:
                count += 1
        return count

s=Solution()
print(s.countDigits(7))
        
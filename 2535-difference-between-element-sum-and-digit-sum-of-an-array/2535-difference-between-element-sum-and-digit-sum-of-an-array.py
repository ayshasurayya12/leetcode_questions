class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elementSum = sum(nums)
        digitSum = 0

        for num in nums:
            for digit in str(num):
                digitSum += int(digit)
        return abs(elementSum - digitSum)

s=Solution()
print(s.differenceOfSum([1,15,6,3]))

        
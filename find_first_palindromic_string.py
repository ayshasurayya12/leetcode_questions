# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

# A string is palindromic if it reads the same forward and backward.

class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for word in words:
            if word == word[::-1]:
                return word        
        return ""
               
s=Solution()
print(s.firstPalindrome(["abc","car","ada","cool","racecar"]))
            
        
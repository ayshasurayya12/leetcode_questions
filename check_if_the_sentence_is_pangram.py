# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        # return len(set(sentence))==26
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch not in sentence:
                return False
        return True
            

s=Solution()
print(s.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
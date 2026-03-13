class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
    
        allowedSet = set(allowed)
        count = 0

        for word in words:
            isConsistent = True
            for ch in word:
                if ch not in allowedSet:
                    isConsistent = False
                    break
            if isConsistent:
                count+=1
        return count

s= Solution()
print(s.countConsistentStrings("ab",["ad","bd","aaab","baa","badab"]))
    
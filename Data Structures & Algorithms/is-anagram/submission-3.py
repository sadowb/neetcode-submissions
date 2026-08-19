class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            print(s)
            print(t)
            return True
        else:
            return False
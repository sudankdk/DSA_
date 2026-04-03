class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_string= sorted(s)
        second_string= sorted(t)
        if first_string== second_string:
            return True

        else:
            return False
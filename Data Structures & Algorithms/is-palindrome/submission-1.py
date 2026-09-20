class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        last = len(s) - 1
        s = s.lower()
        while first < last:
            if not(s[first].isalnum()):
                first += 1
                continue

            if not(s[last].isalnum()):
                last -= 1
                continue

            if not(s[first] == s[last]):
                return False
            
            first += 1
            last -= 1
        return True
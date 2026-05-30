class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s =  "".join(ch.lower() for ch in s if ch.isalnum())
        start = 0
        end = len(new_s) -1
        while start < end:
            if new_s[start] != new_s[end]:
                return False
            start +=1
            end -=1
        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_front = ""

        for char in s:
            if (ord(char)>=ord('a') and ord(char)<=ord('z')) or (ord(char)>=ord('0') and ord(char)<=ord('9')):
                s_front += char

        return s_front==s_front[::-1]
        
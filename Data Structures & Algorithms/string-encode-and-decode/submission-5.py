class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for string in strs:
            ans += str(len(string))+ "$" +string

        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i, start = 0, 0

        while i<len(s):
            while s[i]!="$":
                i+=1
            ans.append(s[i+1: i+1+int(s[start: i])])
            start = i+1+int(s[start: i])
            i = start

        return ans
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        dic1, dic2 = {}, {}

        for i in range(len(s)):
            if s[i] in dic1:
                dic1[s[i]]+=1
            else:
                dic1[s[i]]=1

            if t[i] in dic2:
                dic2[t[i]]+=1
            else:
                dic2[t[i]]=1

        return dic1==dic2
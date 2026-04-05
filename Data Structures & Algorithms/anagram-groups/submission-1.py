class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for string in strs:
            alpha_count = [0]*26

            for char in string:
                alpha_count[ord(char)-ord('a')] += 1

            if tuple(alpha_count) in ans:
                ans[tuple(alpha_count)].append(string)
            else:
                ans[tuple(alpha_count)] = [string]

        return list(ans.values())
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        dic = {}

        for num in nums:
            if num not in dic:
                dic[num] = num+1

        for num in dic:
            streak = 0

            while num in dic:
                streak+=1

                num = dic[num]

            if streak>ans:
                ans = streak

        return ans
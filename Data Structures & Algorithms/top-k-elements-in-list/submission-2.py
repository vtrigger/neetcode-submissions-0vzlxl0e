class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        ans = []
        for _ in range(k):
            maxi = [float('-inf'), -1]
            for num in dic:
                if dic[num]>=maxi[0]:
                    maxi = [dic[num], num]
            
            ans.append(maxi[1])
            dic.pop(maxi[1])

        return ans
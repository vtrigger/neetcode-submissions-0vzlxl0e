class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1

        hashmap = [[] for _ in range(len(nums)+1)]
        for num in dic:
            count = dic[num]
            hashmap[count].append(num)
            print(num, count)

        needed = k
        ans = []
        i = len(nums)-1
        while needed>0:
            if len(hashmap[i])>needed:
                ans+=hashmap[i][:needed]
                needed = 0
            else:
                ans+=hashmap[i]
                needed -= len(hashmap[i])
            i-=1


        return ans

                

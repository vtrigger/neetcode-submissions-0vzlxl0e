class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i, num in enumerate(nums):
            target = -num
            start, stop = i+1, len(nums)-1

            if i>0 and nums[i]==nums[i-1]:
                continue

            while start<stop:
                summ = nums[start]+nums[stop]
                
                if summ==target:
                    ans.append([num, nums[start], nums[stop]])
                    start+=1

                    while start<stop and nums[start-1]==nums[start]:
                        start+=1

                elif summ>target:
                    stop-=1

                else:
                    start+=1

        return ans

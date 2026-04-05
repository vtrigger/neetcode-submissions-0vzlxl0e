class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lft_prd, rgt_prd = [nums[0]]*n, [nums[-1]]*n

        for i in range(1, n):
            lft_prd[i] = lft_prd[i-1]*nums[i]
            rgt_prd[n-i-1] = rgt_prd[n-i]*nums[n-i-1]

        ans = [0]*n
        for i in range(n):
            if i==0:
                ans[i] = rgt_prd[i+1]

            elif i==n-1:
                ans[i] = lft_prd[i-1]

            else:
                ans[i] = lft_prd[i-1]*rgt_prd[i+1]

        return ans
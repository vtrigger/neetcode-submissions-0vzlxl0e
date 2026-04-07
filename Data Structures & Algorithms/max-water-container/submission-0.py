class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = float('-inf')
        max_idx = 0

        for i in range(len(heights)):
            if heights[i]>maxi:
                maxi = heights[i]
                max_idx = i

        max_2 = float('-inf')
        max2_idx = 0
        for i in range(len(heights)):
            if heights[i]>max_2 and i!=max_idx:
                max2_idx = i
                max_2 = heights[i]

        start, stop = max_idx, max2_idx

        ans = 0
        while start>0 or stop<len(heights)-1:
            ans = max(min(heights[stop], heights[start])*(stop-start), ans)

            if stop<len(heights)-1 and start>0:
                if heights[start-1]>heights[stop+1]:
                    start-=1
                else:
                    stop+=1

            else:
                if start==0:
                    stop+=1
                else:
                    start-=1

        return max(min(heights[stop], heights[start])*(stop-start), ans)

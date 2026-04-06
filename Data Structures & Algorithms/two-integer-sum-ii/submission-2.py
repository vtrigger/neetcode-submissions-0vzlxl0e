class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, stop = 0, len(numbers)-1

        while start<stop:
            summ = numbers[start]+numbers[stop]

            if summ==target:
                return [start+1, stop+1]

            elif summ<target:
                start+=1

            else:
                stop-=1


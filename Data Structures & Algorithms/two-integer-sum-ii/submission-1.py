class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(numbers)):
            num = numbers[i]
            if num not in dic:
                dic[num] = target-num, i+1

        for num in dic:
            if dic[num][0]!=num and dic[num][0] in dic:
                return [dic[num][1], dic[dic[num][0]][1]]

        


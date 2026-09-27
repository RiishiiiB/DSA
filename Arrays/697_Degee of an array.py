class Solution:
    def findShortestSubArray(self, nums):
        first = {}
        count = {}
        degree = 0
        answer = len(nums)
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            count[num] = count.get(num, 0) + 1
            degree = max(degree, count[num])
        for num in count:
            if count[num] == degree:
                length = i = nums.index(num)
                length = nums.index(num)  
                last = len(nums) - 1 - nums[::-1].index(num)
                answer = min(answer, last - length + 1)
        return answer
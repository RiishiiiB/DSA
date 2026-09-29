class Solution:
    def deleteAndEarn(self, nums):
        max_num = max(nums)
        points = [0] * (max_num + 1)
        for num in nums:
            points[num] += num
        prev2 = 0
        prev1 = 0
        for i in range(1, max_num + 1):
            current = max(prev1, prev2 + points[i])
            prev2 = prev1
            prev1 = current
        return prev1
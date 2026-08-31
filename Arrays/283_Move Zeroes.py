class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = []
        for num in nums:
            if num != 0:
                result.append(num)
        while len(result) < len(nums):
            result.append(0)
        for i in range(len(nums)):
            nums[i] = result[i]
        
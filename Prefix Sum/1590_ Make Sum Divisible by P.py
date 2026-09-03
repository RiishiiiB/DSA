class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        required = total_sum % p
        if required == 0:
            return 0
        prefix = 0
        seen = {0: -1}
        min_length = len(nums)
        for i in range(len(nums)):
            prefix = (prefix + nums[i]) % p
            needed = (prefix - required) % p
            if needed in seen:
                min_length = min(min_length, i - seen[needed])
            seen[prefix] = i
        if min_length == len(nums):
            return -1
        return min_length
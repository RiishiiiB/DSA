class Solution:
    def subarraySum(self, nums, k):
        prefix = 0
        count = {0: 1}
        ans = 0
        for num in nums:
            prefix += num
            needed = prefix - k
            if needed in count:
                ans += count[needed]
            count[prefix] = count.get(prefix, 0) + 1
        return ans
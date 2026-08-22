class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        ones = 0
        for num in nums:
            ones = ones + 1 if num else 0
            ans = max(ans, ones)
        return ans
        
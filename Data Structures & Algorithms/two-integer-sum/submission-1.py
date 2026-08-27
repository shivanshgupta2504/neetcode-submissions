class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # More optimized: using dict
        temp = {}
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in temp:
                return [temp[remainder], i]
            temp[num] = i
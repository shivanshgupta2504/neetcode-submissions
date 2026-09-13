class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prefix = [1]
        postfix = [1]
        n = len(nums)
        for i in range(1, n):
            value = nums[i-1] * prefix[i-1]
            prefix.append(value)
        nums = nums[::-1]
        for i in range(1, n):
            value = nums[i-1] * postfix[i-1]
            postfix.append(value)
        postfix = postfix[::-1]
        for i in range(n):
            ans.append(prefix[i] * postfix[i])
        return ans

        
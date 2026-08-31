class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i

        n = len(nums)
        nums.sort()
        for i in range(n):
            if nums[i] != i:
                return i
        return n
        
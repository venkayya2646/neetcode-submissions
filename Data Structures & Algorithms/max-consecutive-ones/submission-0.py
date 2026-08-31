class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        c=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
                if c>m:
                    m=c
            else:
                c=0
        return m

        
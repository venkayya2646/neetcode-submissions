class Solution:
    # def prod(self,l):
    #     p=1
    #     for i in range(len(l)):
    #         p=p*l[i]
    #     return p

    def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     m = 1
    #     out = []
    #     for i in range(len(nums)):
    #         m = self.prod(nums[:i]) * self.prod(nums[i+1:])
    #         out.append(m)
    #     return out
        # n = len(nums)
        # res = [0] * n

        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         prod *= nums[j]

        #     res[i] = prod
        # return res
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt +=  1
        if zero_cnt > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt: res[i] = 0 if c else prod
            else: res[i] = prod // c
        return res
        

        
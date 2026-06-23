class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[1]*n
        prod=1
        for i in range(n):
            a[i]=prod
            prod*=nums[i]
        prod=1
        for i in range(n-1,-1,-1):
            a[i]*=prod
            prod*=nums[i]
        return a
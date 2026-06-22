class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     count=0
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #               count+=1
        #     if count>0:
        #         return True
        # return False


        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
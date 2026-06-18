class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k%=n
    
        def reverse_section(start: int, end: int) -> None:
            while start < end:
                
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
    
        reverse_section(0, n - 1)
        reverse_section(0, k - 1)
        reverse_section(k, n - 1)

        


        
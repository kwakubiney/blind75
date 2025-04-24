#O(N) T
#O(N) s
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        recordOfExistingInts = {}
        for element in nums:
            if element in recordOfExistingInts.keys():
                return True
            else:
                recordOfExistingInts[element] = 100
        return False
    
#This also worjs but in 0(1) space complexity
class SecondSolution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = 0, r = 1
        nums = sorted(nums)
        while l <= len(nums) - 1 or r <= len (nums) - 1:
            if nums[l] == nums[r]:
                return True
            l += 1
            r += 1
        return False


    


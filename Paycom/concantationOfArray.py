# problem: 1929 concantation of array 
# given array nums, create another array that is basically joining both arrays
# EX: nums = [1, 2, 3] 
#     output: nums = [1, 2, 3, 1, 2, 3]

# Solution
# we initialize another array and create a for loop that iterates over nums and appends nums[i] to ans
# then we iterate over nums again but append ans[i] to nums then return nums

# Time Complexity: O(n) 
# This is still constant time becase we have two for loops that are not nested

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
     
        for i in range(len(nums)):
            ans.append(nums[i])
        
        for i in range(len(nums)):
            nums.append(ans[i])
        return nums
    
    # or you can literally just return nums + nums
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
      

    

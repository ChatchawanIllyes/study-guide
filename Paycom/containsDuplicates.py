# Given an array nums, check if array has duplicates

# Solution
# Use hashmap to keep track of duplicates, iterate over nums and add into hash, if seen, increment by 1
# Return Fales if there are no duplicates else return true

# Time Complexity: O(n)
# This is because he for loops aren't nested and they run one at a time  

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        
        for i in range(len(nums)): #iterates over nums
            if nums[i] not in hash:  #code to save nums in hash if unique, else adds 1
                hash[nums[i]] = 1 
            else:
                hash[nums[i]] += 1

        for i in hash:
            if hash[i] > 1:
                return True
          
        return False
        




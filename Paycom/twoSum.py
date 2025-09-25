# We are given an array of int nums and we need to return two indices were they add up to target
# EX: nums = [2, 7, 11, 15] Target = 9

# Solution
# We can iterate through nums while keeping in mind of the index and value using enumerate
# Then, since we just need to find the difference value in hash, we can do target - value to get diff
# Then check if thats in the hash, if it is, we can return that index plus the index used to subract from target
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i, v in enumerate(nums):
            diff = target - v
            if diff in hash:
                return (hash[diff], i)
            else:
                hash[v] = i


    

           

            
            
                
           



        
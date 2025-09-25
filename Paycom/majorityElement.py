# Given an array nums and size n, find majority element
# Solution:
# Initialize major by dividing the length of nums by 2, and intialize hash, then interating through array and creating hash
# then we iterate through hash and check if hash[i] is greater than major, if so we turn that

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        major = len(nums) // 2

        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = 1
            else:
                hash[nums[i]] += 1

        for num in hash:
            if hash[num] > major:
                return num
  

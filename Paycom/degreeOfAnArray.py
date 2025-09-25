# given array nums, find the shortest subarray
# solution:
# initialize 3 hashmaps (count, start, end), create a hashmap count then have an if statement that adds to hash start and end and initializes it to i
# else, initialize hashmap end with i 
# then you want to initialize res with len of nums and degree with the max count of values
# afterwards, iterate through count and if count[i] eqauls the degree, then res = min of res and end[i] - start[i] + 1
# then return res

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}
        start = {}
        end = {}

        for i in range(0, len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1

            if nums[i] not in start:
                start[nums[i]] = i
                end[nums[i]] = i
            else:
                end[nums[i]] = i

        
        res = len(nums)
        degree = max(count.values())
        for i in count:
            if count[i] == degree:
                res = min(res, end[i] - start[i] + 1)
        return res
        
        


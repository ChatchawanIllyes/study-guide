# given an array and val (value), remove occurence of value in-place without requiering extra space
# EX:
# nums = [3, 2, 2, 3]
# return k and [2, 2,_,_]

#solution
# we initialize a pointer starting at 0, then when we interate through nums, if nums doesnt equal to value, then we replace nums[l] == num[i]
# then we increment the pointer and return pointer

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[l] = nums[i]
                l += 1
        return l


            


            
        



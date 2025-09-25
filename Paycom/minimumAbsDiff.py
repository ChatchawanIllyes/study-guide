# we are given an array, we must find all pairs of elements with the minimum absolute difference between them
# EX: arr = [4, 2, 1, 3]
# Output: [[1,2], [2,3], [3,4]]

# Solution
# we can sort the array first, arr.sort(), then sent a minimum difference to float('inf') to initialize it, plus initialize res = []
# after that, we iterate through arr but at from (1, len(arr)) <--- this is because it will create a fixed sliding window of two
# so we can compare the digits next to each other since our arr is already sorted
# then to find the curr, you subtract abs(arr[i] - arr[i - 1]) which will give you the curr, 
# next, if minimum diff > curr, we set mini diff to curr then res = [[arr[i - 1], arr[i]]]
# but if the minimum diff is is equal to curr, we res.append([arr[i - 1], arr[i]])
# then return res

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        res = []
        for i in range(1, len(arr)):
            curr = abs(arr[i] - arr[i - 1])
            if min_diff > curr:
                min_diff = curr
                res = [[arr[i-1], arr[i]]]
            elif min_diff == curr:
                res.append([arr[i - 1], arr[i]])

        return res
        
        

        
            

        
# Given a list of strings, return the longest common prefix (portion of the string starting from beginning)
# EX: strs = [flower, flow, flight ]
# return "fl"

# Solution: we can use the reference string (first string) and then interate through the len of that string, while iterating, we use another
# loop to iterate through every other string and compare it with the first string at ith index
# if i == len(s) or s[i] != strs[0][i] then we return res
# else we had strs[0][i] to res our res and continue

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
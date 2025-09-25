#given two strings, return true if they are anagrams of each other (rearrange string into the same string)

# Solution
# We can sort both strings using string manipulation sorted_s = "".join(sorted(s))
# This basically gives us strings sorted in alphabetical order
# Sort for both strings and just compare if they are equal, if so, return true, else false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))

        if sorted_s == sorted_t:
            return True
        else:
            return False

# another solution thats better if can remember

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #checks if the lengths are equal, if not return false
            return False
        
        hash = {}

        for c in s:
            hash[c] = hash.get(c, 0) + 1 #adds to hashmap

        for c in t:
            if c not in hash:
                return False
            hash[c] -= 1
            if hash[c] == 0:
                del hash[c]

        return True

        
        



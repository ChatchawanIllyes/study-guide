#given an array of strs, group anargrams together and return them in a list of any order
# Solution:
# You iterate through strs while having count = [] of 26 letters (a-z)
# then you iterate through s (for c in s) and then convert c into unicode using ord() then subtract that with ord("a") to get count of each letter in string
# then convert count to a tuple and append it to res, then return the list of res.values()


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary where each key maps to a list of strings
        # defaultdict(list) automatically creates an empty list for a new key
        res = defaultdict(list)

        # Loop through each string in the input list
        for s in strs:
            # Create a list of 26 zeros to count each letter 'a' to 'z'
            count = [0] * 26

            # Count the frequency of each character in the current string
            for c in s:
                # ord(c) - ord('a') converts 'a' -> 0, 'b' -> 1, ..., 'z' -> 25
                count[ord(c) - ord("a")] += 1

            # Use the tuple of counts as the dictionary key and append the string
            # All anagrams will have the same count tuple
            res[tuple(count)].append(s)

        # Return all the grouped anagrams as a list of lists
        return list(res.values())
# [455] https://leetcode.com/problems/assign-cookies/
# Assign cookies to children to maximize the number of content children.
def findContentChildren(g, s):
    g.sort()
    s.sort()
    i = j = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            i += 1
        j += 1
    return i


# [435] https://leetcode.com/problems/non-overlapping-intervals/
# Find the minimum number of intervals to remove to make the rest non-overlapping.
def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])
    end = intervals[0][1]
    count = 1
    for i in range(1, len(intervals)):
        if intervals[i][0] >= end:
            end = intervals[i][1]
            count += 1
    return len(intervals) - count


# [122] https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Maximize profit by buying and selling stocks multiple times.
def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit


# [134] https://leetcode.com/problems/gas-station/
# Find the starting gas station to complete a circular route.
def canCompleteCircuit(gas, cost):
    total_tank = current_tank = start = 0
    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        current_tank += gas[i] - cost[i]
        if current_tank < 0:
            start = i + 1
            current_tank = 0
    return start if total_tank >= 0 else -1

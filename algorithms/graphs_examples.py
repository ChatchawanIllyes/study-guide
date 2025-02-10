# [207] https://leetcode.com/problems/course-schedule/
# Check if it's possible to finish all courses given prerequisites.
def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * numCourses
    for u, v in prerequisites:
        graph[v].append(u)
        in_degree[u] += 1
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    count = 0
    while queue:
        node = queue.popleft()
        count += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return count == numCourses


# [210] https://leetcode.com/problems/course-schedule-ii/
# Find the order of courses to take given prerequisites.
def findOrder(numCourses, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * numCourses
    for u, v in prerequisites:
        graph[v].append(u)
        in_degree[u] += 1
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return result if len(result) == numCourses else []


# [133] https://leetcode.com/problems/clone-graph/
# Clone a connected undirected graph.
def cloneGraph(node):
    if not node:
        return None
    visited = {}
    def dfs(node):
        if node in visited:
            return visited[node]
        clone = Node(node.val, [])
        visited[node] = clone
        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))
        return clone
    return dfs(node)

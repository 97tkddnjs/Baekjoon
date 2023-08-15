from collections import deque



dx = [1,-1,0,0]
dy = [0,0,1,-1]

visited= set()

def bfs(visited, graph):
    queue = deque()
    queue.append((0,0))

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



def dfs(visited, graph):

    visited

    pass


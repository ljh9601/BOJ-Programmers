from collections import deque

def bfs(n, m):
    visited = [0] * 100001
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        if x == m:
            return visited[x]
        for i in (x-1, x+1, 2 * x):
            if i >= 0 and i <= 100000:
                if visited[i] == 0:
                    visited[i] = visited[x] + 1
                    queue.append(i)
                    
    return visited[m]

if __name__ == "__main__":
    n, m = list(map(int, input().split()))

    print(bfs(n, m))


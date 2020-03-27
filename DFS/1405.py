import sys

result = 0.0
visited = [[False] * 29 for i in range(29)]

def dfs(start, count, total, num, prob):
    global result 
    y, x = start[0], start[1]
    visited[y][x] = True
    
    if (count == num):
        result += total
    
    if (count < num and not visited[y-1][x]):
        dfs((y - 1, x), count + 1, total * prob[3] / 100, num, prob)
    if (count < num and not visited[y+1][x]):
        dfs((y + 1, x), count + 1, total * prob[1] / 100, num, prob)
    if (count < num and not visited[y][x-1]):
        dfs((y, x - 1), count + 1, total * prob[2] / 100, num, prob)
    if (count < num and not visited[y][x+1]):
        dfs((y, x + 1), count + 1, total * prob[0] / 100, num, prob)
 
    visited[y][x] = False

if __name__ == "__main__":
    num, e, w, s, n = map(int, sys.stdin.readline().strip().split())
    prob = []
    prob.append(e)
    prob.append(s)
    prob.append(w)
    prob.append(n)
    start = (14, 14)
    dfs(start, 0, 1.0, num, prob)

    print(round(result, 9))
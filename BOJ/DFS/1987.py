# 풀이일자 : 2020/04/08
# 문제 이름 : 알파벳
# 문제 번호 : 1987
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : DFS
# 말이 지날 수 있는 최대의 칸 수
# 반복적 DFS로 할 경우 백트래킹이 복잡해지기 때문에 재귀 형식으로 품. 다만 python3로 채점하면 시간 초과가 나니 PyPy3로 채점해야 함.
# check 함수를 만들어서 ord 함수를 통해 알파벳 중복 여부를 확인하는 것이 핵심!

import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
ans = -1
def dfs(posX, posY, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = posX + dx[i]
        ny = posY + dy[i]
        if 0 <= nx < n and 0 <= ny < m :
            cur = ord(board[nx][ny]) - ord('A')
            if not check[cur]:    
                check[cur] = True
                dfs(nx, ny, cnt + 1)
                check[cur] = False

n, m = map(int, sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]
check = [False] * 26
check[ord(board[0][0]) - ord('A')] = True
dfs(0, 0, 1)
print(ans)
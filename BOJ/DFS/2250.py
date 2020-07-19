# 풀이일자 : 2020/05/05
# 문제 이름 : 트리의 너비와 높이
# 문제 번호 : 2250
# 작성자 : 이장행
# 문제 출처 : 백준 온라인 저지
# 알고리즘 분류 : DFS
# 이진트리에서 가장 너비가 넓은 레벨
# 이진 트리의 Inorder Traverse 를 통해 너비의 최댓값을 갱신시켜야 함
# 출처 : https://codingfull.tistory.com/29 를 99퍼 이상 참고.
# 문제가 된다면 삭제하겠습니다.
import sys

order = 0

class Node :
    def __init__(self) :
        self.left = self.right = -1
        self.depth = self.order = 0

def inorder(node, depth):
    global order
    if node == -1:
        return
    inorder(a[node].left, depth+1)
    a[node].depth = depth
    order += 1
    a[node].order = order
    inorder(a[node].right, depth+1)

nodeNum = int(sys.stdin.readline().strip())
a = [Node() for _ in range(10001)]
left = [0]*10001
right = [0]*10001
parent = [0]*10001
for i in range(nodeNum):
    x, b, c = map(int, sys.stdin.readline().split())
    a[x].left = b
    a[x].right = c
    if b != -1:
        parent[b]+=1
    if c != -1:
        parent[c]+=1
root = 0
for i in range(1, nodeNum+1):
    if parent[i] == 0:
        root = i
inorder(root, 1)
maxdepth = 0
for i in range(1, nodeNum+1):
    depth = a[i].depth
    order = a[i].order
    if left[depth] == 0:
        left[depth] = order
    else:
        left[depth] = min(left[depth], order)
    right[depth] = max(right[depth], order)
    maxdepth = max(maxdepth, depth)

maxwidth = 0
anslevel = 0

for i in range(1, maxdepth+1):
    if maxwidth < right[i] - left[i] + 1:
        maxwidth = right[i]-left[i]+1
        anslevel = i
sys.stdout.write("{} {}".format(anslevel, maxwidth))
'''
#BFS
-> 탐색 문제일 때 최단 경로를 구하려면 BFS
-> 어지간하면 DFS 말고 BFS로 (탐색 속도 차이가 큼)
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def solutions(board, start, end) :
    #n * m 크기의 board라고 가정
    q = deque()
    visited = [[0] * m for _ in range(n)]
    visited[start[0]][start[1]] = 1
    q.appendleft(start)
    while q :
        x, y = q.popleft()
        if [x, y] == end :
            return visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if not visited[nx][ny] :
                    visited[nx][ny] = True
                    q.append([nx, ny])
    return -1
'''

'''
#DFS
-> 모든 경로를 탐색해야만 하고 재귀를 사용한 식이 편할 때만 쓰자
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def solutions(board, start, end) :
    #n * m 크기의 board라고 가정
    stack = deque()
    visited = [[0] * m for _ in range(n)]
    visited[start[0]][start[1]] = 1
    stack.appendleft(start)
    while stack :
        x, y = stack.pop()
        if [x, y] == end :
            return visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if not visited[nx][ny] :
                    visited[nx][ny] = True
                    stack.append([nx, ny])
    return -1
'''

'''
# Binary Search
-> 배열 내에서 값을 찾아야 하는데 배열의 크기가 방대할 때 사용하면 매우 빠름
-> 항상 Sort된 상태에서 시작돼야 한다는 것을 명심(단조 증가 수열이어야 한다.)
-> 낮에는 올라가고 밤엔 떨어지는데 지정한 높이까지 며칠 걸리는지 이런 문제에 사용 가능(결국 하루마다 올라가긴 하므로 단조 증가이기 때문)
-> 초기 left와 right 설정이 매우 중요하다
-> lower bound와 upper bound 모두 이분탐색의 아주 살짝 변형
-> lower bound : 찾고자(넣고자) 하는 원소가 나타나는 첫 위치
-> upper bound : 찾고자 하는 원소보다 큰 값이 나타나는 첫 위치
#이분탐색
def solutions(sortedArr, left, right, val):
    while left < right :
        mid = (left + right) // 2
        if sortedArr[mid] == val :
            return mid
        elif sortedArr[mid] > val : #현재 찾고자 하는 값보다 오른쪽에 있는 경우
            right = mid - 1
        else : #현재 찾고자 하는 값보다 왼쪽에 있는 경우
            left = mid + 1
#lower bound
-> Python 유저라면 bisect_left(집어넣을 배열, 넣으려고 하는 값, low, high) 을 사용하자 -> low, high는 디폴트값이 배열의 처음과 끝, 범위 지정은 선택
-> from bisect import bisect_left
def solutions(sortedArr, left, right, val):
    while left < right :
        mid = (left + right) // 2
        if sortedArr[mid] < val :
            left = mid + 1
        else : 
            right = mid
    return high + 1

#upper bound
-> Python 유저라면 bisect_right(집어넣을 배열, 넣으려고 하는 값) 을 사용하자
-> from bisect import bisect_right
def solutions(sortedArr, left, right, val):
    while left < right :
        mid = (left + right) // 2
        if sortedArr[mid] <= val :
            left = mid + 1
        else : 
            right = mid
    return high + 1
-> lower bound와 upper bound의 차이점은 단지 부등호의 한끗 차이

'''
'''
플로이드 알고리즘 
-> 최단 경로(최소 비용)를 찾고 싶을 때 가장 간단하게 짤 수 있음 
-> 최악의 경우 O(N^3)이지만 코드가 매우 간결해서 시간 없을 때 사용 가능
-> n * n 배열일 때만 사용 가능
-> 여러 도시가 있고, 어떤 도시에서 어떤 도시로 갈 수 있는지 여부 등이 주어질 때 사용 가능
import sys

def solutions(arr): -> 여기서 arr[i][j]는 i번에서 j번으로 갈 수 있는지 여부임(cost도 가능)
    floyd = [[sys.maxsize] * n for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j :
                    arr[i][j] = 0
                else :
                    arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
'''

'''
# 다익스트라 알고리즘
-> 인접 행렬과 시작 정점이 주어졌을 때, 시작 정점에서 모든 정점으로 가는 최단 거리(최소 비용) 구할 수 있음
-> priority queue, heap 이용
def solutions(adjacent, K):
    prev = [-1] * (len(adjacent) + 1)
    dist = [sys.maxsize] * (len(adjacent) + 1)   # source로부터의 최소 거리 배열
    dist[K] = 0
    priority_queue = []
    heapq.heappush(priority_queue, [0, K])
    while priority_queue:
        # 거리가 제일 작은 노드 선택
        current_dist, here = heapq.heappop(priority_queue)
        # 인접 노드 iteration
        for there, length in adjacent[here].items():
            next_dist = dist[here] + length
            if next_dist < dist[there]:
                dist[there] = next_dist
                prev[there] = here
                heapq.heappush(priority_queue, [next_dist, there])
    return dist, prev
'''

'''
코테 저격용 DP
-> 최근 문자열 처리가 코테에서 많이 나오므로 LCS(최장 공통 부분 수열), LIS(최장 증가 수열)에 대해서 알 필요가 있음
-> dp로 풀면 O(N^2)
-> LIS의 경우 lower bound를 통해 O(N log N)으로 가능
#LCS
#두 문자열 간의 최장 공통 부분 수열
A = "ACAYKP"
B = "CAPCAK"
def solutions(A, B):
    lcs = [[0 for i in range(len(A)+1)] for j in range(len(B)+1)]
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])
                            
    return lcs[-1][-1]


#LIS
#한 문자열 내 최장 증가 부분 수열

# DP로 해결할 경우(O(N^2))
def solutions():
    for i in range(1,n+1):
        for j in range(1, i):
            if a[i] > a[i-j]:
                DP[i] = max(DP[i-j], DP[i])
        DP[i] += 1
    return max(DP)

# lower bound를 이용해 해결할 경우(O(N log N))
from bisect import bisect_left
arr= [3,1,2,4,8,6,7]

def solutions():     
    n= len(arr)
    dp= [arr[0]]
 
    for i in range(1, n):
        if dp[-1] < arr[i]:
            dp.append(arr[i])
        else:
            dp[bisect_left(dp, arr[i])]= arr[i]
    res= max(dp)
'''

'''
#이진 탐색 트리 구현
-> 혹시 몰라서 추가

class Node(object):
    def __init__(self, data):
    self.data = data
    self.left = self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
            return self.root is not None
    
    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)
    
    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted
    
    def _delete_value(self, node, key):
        if node is None:
            return node, False
        
        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

    -> 전위 순회일 경우 : print root -> order root.left -> order root.right
    -> 중위 순회일 경우 : order root.left -> print root -> order root.right
    -> 후위 순회일 경우 : order root.left -> order root.right -> print root
    def order_traversal(self): 
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                print(root.data)
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
        _pre_order_traversal(self.root)


array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]
bst = BinarySearchTree()
for x in array:
    bst.insert(x)
# Find
print(bst.find(15)) # True
print(bst.find(17)) # False
# Delete
print(bst.delete(55)) # True
print(bst.delete(14)) # True
print(bst.delete(11)) # False

비트 연산자
^(xor) 연산은 두개의 값이 다를 때만 참인 연산입니다.
~(not) 연산은 1의 보수를 구합니다. 컴퓨터에서는 뺄셈을 2의 보수를 덧셈하여 처리 합니다.
<< 연산은 왼쪽으로 1비트 밀때마다 두 배씩 늘어납니다.
>> 연산은 오른쪽으로 1비트 밀때마다 1/2씩 줄어듭니다.
n << m : n * 2의 m승
n >> m : n / 2의 m승
'''
lost = []
lost.pop()
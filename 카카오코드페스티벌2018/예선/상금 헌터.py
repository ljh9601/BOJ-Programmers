import sys
from collections import defaultdict

# key : 등수
# value : 상금
festival_a = defaultdict(int)
festival_b = defaultdict(int)

# 각 페스티별 등수 당 상금
reward_a = [0, 500, 300, 200, 50, 30, 10]
reward_b = [0, 512, 256, 128, 64, 32]

# 각 페스티벌의 등수
rank_a = len(reward_a) - 1
rank_b = len(reward_b) - 1

# 각 페스티벌 당 수상자 수 합계
num_a = sum([v for v in range(1, 7)]) # 1 + 2 + 3 + 4 + 5 + 6 = 21
num_b = sum([2 ** v for v in range(5)]) # 32 + 64 + 128 + 256 + 512 = 992

cnt = 1
for i in range(1, rank_a + 1):
    for j in range(cnt, i+cnt):
        festival_a[j] = reward_a[i]
    cnt += i

cnt, idx = 1, 1
while idx <= rank_b :
    for i in range(cnt, (cnt*2)):
        festival_b[i] = reward_b[idx]
    cnt *= 2
    idx += 1

tc = int(sys.stdin.readline().strip())
for _ in range(tc):
    a, b = map(int, sys.stdin.readline().strip().split())
    print((festival_a[a] + festival_b[b]) * 10000)

        
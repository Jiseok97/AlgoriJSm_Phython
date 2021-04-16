import sys

input = sys.stdin.readline
N, W = map(int, input().split())
bag = [tuple(map(int, input().split())) for _ in range(N)]
# 튜플은 원소의 값 변경 불가능
# 튜플 (), 리스트 []

knap = [0 for _ in range(W+1)]

for i in range(N):
    for j in range(W, 1, -1):
        if bag[i][0] <= j:
            knap[j] = max(knap[j], knap[j-bag[i][0]] + bag[i][1])

print(knap[-1])
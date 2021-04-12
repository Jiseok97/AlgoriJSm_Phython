# 원형
# f(n) = 1 + min(f(n/3), f(n/2), f(n-1))

import math, sys  # inf 사용(무한대, 엄청 큰 값 의미)
input = sys.stdin.readline

n = int(input())
lst = [0, 0, 1, 1, 2]  # 0 ~ 4 까지의 최소 횟수
for i in range(5, n + 1):
  a, b, c = math.inf, math.inf, lst[i - 1]  # min으로 뽑는거니까 없으면 그냥 큰 값 입력해서 없애버리기
  if i % 3 == 0:
    a = lst[i//3]
  if i % 2 == 0:
    b = lst[i//2]
  lst.append(1 + min(a, b, c))

print(lst[n])
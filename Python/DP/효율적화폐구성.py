n, m = map(int, input().split())
lst = []

for i in range(n):
  lst.append(int(input()))

# 계산된 결과를 저장하기 위한 DP 테이블
d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
  for j in range(lst[i], m + 1):
    if d[j - lst[i]] != 10001:  # (i - k)원 가능한 경우
      d[j] = min(d[j], d[j - lst[i]] + 1)

if d[m] == 10001:  # 최종적으로 M원을 만드는 경우 없을 때
  print(-1)
else:
  print(d[m])
n, m = map(int, input().split())
lst = []

for i in range(n):
  lst.append(int(input()))

# 계산된 결과를 저장하기 위한 DP 테이블
d = [10001] * (m + 1)

d[0] = 0
for i in range(n):  # 각각의 화폐의 단위 의미
  for j in range(lst[i], m + 1):  # 각각의 금액 의미  
    # 기존의 방법이 존재하는 경우의 값을 늘려가며 진행
    # d[j - lst[i]] -> 현재의 금액에서 현재 확인하고 있는 화폐 단위의 금액을 뺀 그 금액을 만들 수 있다면 = (i - k)원 가능한 경우
    if d[j - lst[i]] != 10001:
      d[j] = min(d[j], d[j - lst[i]] + 1)  # 뒤에 +1은 나누어 딱 떨어질 경우에도 한 횟수를 쳐줘야되서 해줌

if d[m] == 10001:  # 최종적으로 M원을 만드는 경우 없을 때
  print(-1)
else:
  print(d[m])
n = int(input())
# 모든 식량 정보 입력 받기
lst = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1000

# DP(보텀업)
d[0] = lst[0]
d[1] = max(lst[0], lst[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + lst[i])

print(d[n - 1])


# 조건을 만족하지 못하는 내가 푼 코드
n = int(input())
lst = list(map(int, input().split()))
lst2 = []
num1 = 0
num2 = 0
result = 0

for i in lst:
  lst2.append(i)
lst2.sort(reverse=True)

num1 = lst2[0]
num2 = lst2[1]

for i in range(n):
  if lst[i] == num1 or lst[i] == num2:
    result += lst[i]

print(result)




# 시각
# 정수 N이 입력되면 00시00분00초부터 N시59분59초까지의 모든 시각 중에서
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램

# 입력 예시: 5
# 출력 예시: 11475

# 내가 푼 코드 (못품)

# n = int(input())
# check = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]
# result = 0

# for h in range(n+1):
#   for m in range(60):
#     for s in range(60):
#       for i in range(len(check)):
#           if h == check[i] or m == check[i] or s == check[i]:
#             result += 1
       

# print(result)


# 동빈나 코드

# H 입력 받기
h = int(input())

count = 0
for i in range(h + 1):
  for j in range(60):
    for k in range(60):
      # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가 (시간, 분, 초를 문자열로 다 합쳐 버리고 모색)
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)
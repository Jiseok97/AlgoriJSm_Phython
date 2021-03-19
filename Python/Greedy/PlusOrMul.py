# 곱하기 혹은 더하기

# 0 ~ 9까지 수가 문자열 S로 주어짐
# 숫자 사이에 +, * 연산자로 가장 큰 값을 구하는 프로그램

# 내가 푼 코드

import sys

s = sys.stdin.readline().rstrip()
total = 0
listNumber =  sorted(list(map(int, s)),reverse= True)

for i in range(len(listNumber)):
  if listNumber[i] <= 1:
    total += listNumber[i] 
  else:
    if total == 0:
      total += 1
    total *= listNumber[i]

print(total)


# 동빈나 코드

# data = input()

# # 첫 번째 문자를 숫자로 변경하여 대입
# result = int(data[0])

# for i in range(1, len(data)):
#   # 두 수 중에서 하나라도 '0' 혹은 '1' 인 경우, 곱하기보다는 더하기 수행
#   num = int(data[i])
#   if num <= 1 or result <= 1:
#     result += num
#   else:
#     result *= num

# print(result)
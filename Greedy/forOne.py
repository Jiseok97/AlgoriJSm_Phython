# 1이 될 때까지
# N = 25, K = 5 일 때, -1을 하거나 K로 나누어서 1이 되는 최소 횟수 구하기
# 입력 예시: 25 5

# 예로 n = 25, k = 3 가정
# 내가 푼 코드

n, k = map(int, input().split())
count = 0

while True:
  if n != 1:
    if n % k == 0:
      n //= k
      count += 1
    else:
      n -= 1
      count += 1
  else:
    break

print(count)
    

# 동빈나 코드

# # N, K을 공백을 기준으로 구분하여 입력 받기
# n, k = map(int, input().split())

# result = 0

# while True:
#   # N이 K로 나누어 떨어지는 수가 될 때 까지 빼기
#   target = (n // k) * k
#   result += (n - target)
#   n = target
  
#   # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
#   if n < k:
#     break
  
#   # K로 나누기
#   result += 1
#   n //= k

# # 마지막으로 남은 수에 대하여 1씩 빼기
# result += (n - 1)
# print(result)
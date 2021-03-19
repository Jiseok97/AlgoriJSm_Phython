# 숫자 카드 게임
# n개의 행과 m개의 열을 가진 2차원 리스트를 주어졌을 때
# 각 행의 최솟값들 중 최댓값 추출하기 

# 입력 예시
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 출력 예시: 2

# 2 4
# 7 3 1 8
# 3 3 3 4

# 출력 예시: 3

# 모범 코드

# n, m을 공백으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력 받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 '가장 작은 수' 찾기
  min_value = min(data)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result) 


# 내가 푼 코드

# n, m = map(int, input().split())

# result = 0
# for i in range(n):
#   array = list(map(int, input().split()))
#   array.sort()
#   result = array[0]
#   if result > array[0] :
#     result = array[0]
# print(result)
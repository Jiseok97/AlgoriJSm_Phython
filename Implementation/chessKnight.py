# 왕실의 나이트
# 수평 or 수직으로 이동하고 대각선으로 한칸 이동 = 나이트 동선
# 이때, 주어지는 위치에서 나이트가 이동할 수 있는 경우의 수 구하기!

# 입력 예시: a1 
# 출력 예시: 2

# 동빈나 코드

# 현재 나이트의 위치 입력 받기
input_data = input()
row = int(input_data[1])
# ord는 문자를 아스키코드 값을 돌려주는 내장함수 원형=> ord(a) -> 97
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1), (-1,-2), (1, -2), (2,-1), (2,1), (1,2), (-1,2),(-2,1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
  # 이동하고자 하는 위치 확인
  next_row = row + step[0]
  next_column = column + step[1]
  # 해당 위치로 이동이 가능하다면 카운트 증가
  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

print(result)




# 내가 푼 코드 (응, 못품)

# import sys
# x, y = 1, 1
# data = sys.stdin.readline().rstrip()

# pan = [[0]*8]*8

# # 왼쪽부터 하나씩 배열을 만들어 봄
# dx = [-3, -1,  1,  3, 3, 1, -1, -3]
# dy = [-1, -3, -3, -1, 1, 3,  3,  1]

# for i in range(8):
#   for j in range(8):

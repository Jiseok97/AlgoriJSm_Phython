 # 상하좌우
# 여행가 A가 최종적으로 도착할 지점(X,Y) 좌표를 공백을 기준으로 구분하여 출력한다
# L, R, U, D 문자가 반복적으로 사용하고, 공간을 벗어나느 움직임은 무시된다

# 입력 예시: 5
# R R R U D D
# 출력 예시: 3 4

# 동빈나 코드

# N 입력 받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
  # 이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  
  # 공간을 벗어나는 경우 무시
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  
  # 이동 수행
  x, y = nx, ny

print(x, y)

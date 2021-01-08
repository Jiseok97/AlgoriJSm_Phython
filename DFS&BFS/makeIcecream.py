# 음료수 얼려 먹기
# N * M 크기의 얼음 틀 중 비어있는 칸(0)이 연결되어 있으면 아이스크림 생성
# 이 때, 생성되는 아이스크림 갯 수 구하기

# 입력 예시: 4 5
# 00110
# 00011
# 11111
# 00000
# 출력 예시: 3 -> 0으로 연결된거 왼쪽 상단 1개, 오른쪽 상단 1개, 하단 1개

# 모범 코드 

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
  # 주어진 범위를 벗어나는 경우에는 즉시 종료
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  # 현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == 0:
    # 해당 노드 방문 처리
    graph[x][y] = 1
    # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return False

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

  # 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    # 현재 위치에서 DFS 수행
    if dfs(i, j) == True:
       result += 1

print(result)  # 정답 출력
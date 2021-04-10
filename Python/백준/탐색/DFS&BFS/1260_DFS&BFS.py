# N = 정점 갯수, M = 간선의 수, V = 시작하는 노드
N,M,V=map(int,input().split())

# 정점 갯수에 맞게 2차원 배열 생성 (전체 틀)
matrix=[[0]*(N+1) for i in range(N+1)]

# 연결되있는 노드들 입력 받기
for i in range(M):
    a,b = map(int,input().split())
    matrix[a][b]=matrix[b][a]=1  # 1,4 일 경우, 4에서도 1을 갈 수 있기 때문

visit_list=[0]*(N+1)  # 방문한 위치를 저장하는 배열

def dfs(V):
    visit_list[V] = 1  # 방문 된 정점을 방문 배열에 체크
    print(V, end=' ')

    for i in range(1, N+1):  # 모든 노드를 확인하기 위한 루프
        # 해당 노드를 방문하지 않았으며, 입력 받은 노드가 간선으로 연결이 되어 있으면
        # 위로 올라가(재귀) 
        
        if(visit_list[i]==0 and matrix[V][i]==1): 
            dfs(i)

def bfs(V):
    queue=[V] #들려야 할 정점 저장
    visit_list[V]=0 #방문한 점 0으로 표시
    while queue:
        V=queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if(visit_list[i]==1 and matrix[V][i]==1):
                queue.append(i)
                visit_list[i]=0

dfs(V)
print()
bfs(V)

# ==============================================================
# ==============================================================
# ==============================================================
# 다른 풀이

def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, n + 1):
        if visit[i] == 0 and s[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = [v]
    visit[v] = 0
    while(queue):
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, n + 1):
            if visit[i] == 1 and s[v][i] == 1:
                queue.append(i)
                visit[i] = 0

n, m, v = map(int, input().split())
s = [[0] * (n + 1) for i in range(n + 1)]
visit = [0 for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1
    
dfs(v)
print()
bfs(v)
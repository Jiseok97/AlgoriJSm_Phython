N = int(input())
dist = list(map(int, input().split()))
costs = list(map(int, input().split()))

minCost = costs[0]  # 처음엔 초기값을 곱해줌
result = 0
for i in range(N-1):  # 마지막꺼는 계산 x
    if minCost > costs[i]:  # 최솟값보다 다음 원소가 작을 경우
        minCost = costs[i]      # 최솟값 해당 원소로 초기화
    result += (minCost * dist[i])   # 결괏값 = 최소 가격 * 앞으로의 거리
    
print(result)
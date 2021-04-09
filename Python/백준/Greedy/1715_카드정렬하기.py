import heapq
import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
  lst.append(int(input()))

result = 0
heapq.heapify(lst)  # heapify -> sort()와 기능이 같음
while len(lst) > 1:
  a = heapq.heappop(lst)    # 첫번째 원소 추출(제일 작은)
  b = heapq.heappop(lst)    # 두번째 원소 추출(2번째로 작은)
  heapq.heappush(lst, a+b)  # 두 원소를 더하고 다시 힙에 넣음
                            # 데이터 추가시, 다시 최솟값으로 정렬함
                            # 매번 추출시마다 최솟값이 먼저 나옴
                            # 최댓값 추출을 원할시 앞에 '-' 붙혀주면 된다고 함
  result += (a+b)

print(result)
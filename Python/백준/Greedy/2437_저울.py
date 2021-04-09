n=int(input())
weight=list(map(int,input().split()))
weight.sort()

target=1
#만들 수 없는 수 찾기
for i in weight:
  if target<i:
    break
  target+=i

print(target)
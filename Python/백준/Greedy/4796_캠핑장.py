import sys
input = sys.stdin.readline

cnt = 1
while 1:
    l, p, v = map(int, input().split())
    if l + p + v == 0:
        break

    res = (v // p) * l
    res += min((v % p), l)
    print('Case %d: %d' % (cnt, res))
    cnt += 1



# 입력과 결과가 하나 일 때
L, P, V = map(int, input().split())
mRes = (V // P) * L
res = V - ((V // P) * P)
day = mRes + res
print(day)


# 시간초과 코드
L, P, V = map(int, input().split())
day = 0
rot = (V // P) + 1
sub = P - L

for i in range(rot):
  for j in range(L):
    if V == 0:
      break
    else:
      V -= 1
      day += 1
  V -= sub

print(day)    
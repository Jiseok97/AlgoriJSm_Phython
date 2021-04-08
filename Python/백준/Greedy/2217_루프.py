N = int(input())
c = []
tot = 0

for i in range(N):
  i = int(input())
  c.append(i)
c.sort(reverse=True)

for i in range(len(c)):
  value = c[i] * (i+1)
  if value > tot:
    tot = value

print(tot)
a, b, c = map(int, input().split())
if c > b:
  c -= b
  total = (a // c) + 1
  print(total)

else:
  print(-1)
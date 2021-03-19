import sys

count = [0] * 10001

for i in range(int(input())):
  temp = int(sys.stdin.readline())
  count[temp] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i)
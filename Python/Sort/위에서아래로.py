n = int(input())
lst = []
for i in range(n):
  lst.append(int(input()))

lst.sort(reverse = True)
# 다른 방법
# 파이썬 기본 정렬 라이브러리르 이용하여 정렬 수행
# lst.sorted(lst, reverse = True)

for i in lst:
  print(i, end=' ')

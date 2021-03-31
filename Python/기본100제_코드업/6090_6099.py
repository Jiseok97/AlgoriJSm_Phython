# 6090
a, m, d, n = map(int, input().split())
total = a

for _ in range(1, n):
  total *= m
  total += d

print(total)



# 6091
a, b, c = map(int, input().split())
day = 1

# a, b, c가 day를 나누었을 때, 나머지가 안남을 때가 최소 공배수와 같은 의미
while day % a != 0 or day % b != 0 or day % c != 0:
  day +=1

print(day)



# 6092
ct = int(input())
students = input().split() 

for i in range(ct):
  students[i] = int(students[i])

# students 번호에 맞는 횟수를 세줄 빈 list 생성
count = []
for i in range(24):
  count.append(0)

# 해당 학생 n번호가 불릴 시 count list의 n번 + 1
for i in range(ct):
  count[students[i]] += 1

# 1번부터 23번까지 총 불린 횟수 출력
for i in range(1, 24):
  print(count[i], end=' ')



# 6093
# 배열의 순서 바꾸기
n = int(input())
number = input().split()

for i in range(n):
  number[i] = int(number[i])

for i in range(n-1, -1, -1):
  print(number[i], end=' ')



# 6094
n = int(input())
a = list(map(int, input().split()))
a.sort()
print(a[0])



# 6095
d = [[0 for j in range(20)] for i in range(20)]  # List Comprehensions
# d의 이차원 배열(20x20)을 아래 코드보다 List Comprehensions로 더 간결하게 표현한 것

# d = []
# for i in range(20):
#   d.append([])
#   for j in range(20):
#     d[i].append(0)

n = int(input())

for i in range(n):
  x, y = input().split()
  d[int(x)][int(y)] = 1

for i in range(1, 20):
  for j in range(1, 20):
    print(d[i][j], end =' ')
  print()




# 6096
# 아직 못 품
a = [[]*19 for _ in range(19)]
for i in range(19):
   a[i]=list(map(int,input().split()))

n = int(input())

for i in range(n):
    b,c=map(int,input().split())
    
    for j in range(19):
        if(a[b-1][j]==1):
            a[b-1][j]=0
        else: a[b-1][j]=1
    
    for j in range(19):
        if(a[j][c-1]==1):
            a[j][c-1]=0
        else: a[j][c-1]=1

for i in range(19):
    for j in range(19):
        print(a[i][j],end=' ')
    print()
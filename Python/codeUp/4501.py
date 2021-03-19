# 코드업 4501번 문제
# 백설공주와 난쟁이

count = 7
people = {}

for i in range(0, count):
  people[i] = int(input())

height = sorted(people.items(), key=lambda t:t[1], reverse=True)

print(height[0][1])
print(height[1][1])

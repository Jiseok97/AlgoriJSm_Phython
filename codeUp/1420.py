# 코드업 1420번 문제
# 3등 찾기

count = int(input())
hash_record = {}

for i in range(0, count):
  name, score = input().split()
  hash_record[name] = int(score)

data = sorted(hash_record.items(), key=lambda t: t[1], reverse=True)
print(data[2][0])
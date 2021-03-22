# 6020
# 정수로 받으면 0097은 97로 표기 되기 때문에 str로 받아야 된다
front, end = map(str, input().split('-'))
print(front+end)

# 6021
# 한 문장을 한 개씩 출력
data = input()
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])

# 6022
data = input()
print(data[0:2], data[2:4],data[4:])

# 6023
hour, minute, second = input().split(':')
print(minute)

# 6024
word1, word2 = input().split()
string = word1 + word2
print(string)
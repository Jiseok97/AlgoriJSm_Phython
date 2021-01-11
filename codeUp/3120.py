# 리모컨

a = input()
b = a.split()
count = 0

if(int(b[0]) < int(b[1])):
  t1 = int(b[0])
  t2 = int(b[1])
else:
  t1 = int(b[1])
  t2 = int(b[0])

temp = t2- t1
while(1):
  if(temp > 7):
    temp -= 10
  elif(temp > 3):
    temp -= 5
  elif(temp >= 1):
    temp -= 1
  elif(temp < 0):
    temp *= -1
    count -= 1
  elif(temp == 0):
    break
  count += 1

print(count)




# temperature = list(map(int, input().split()))

# temp_types = [10, 5, 1]
# count = 0

# if temperature[0] < 0:
#   gap = abs(abs(temperature[1]) + abs(temperature[0]))
# else:
#   gap = abs(abs(temperature[1]) - abs(temperature[0]))


# for i in temp_types:
#   count += gap // i
#   gap %= i

 
# print(count)


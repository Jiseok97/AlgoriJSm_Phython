T = int(input())

for i in range(T):
  data = list(map(int, input().split()))
  
  odd_num = [num for num in data if num % 2 == 1]

  print("#{} {}".format(i+1, sum(odd_num)))
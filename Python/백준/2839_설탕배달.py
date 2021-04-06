n = int(input())
bag = 0
while n >= 0:
  if n % 5 == 0:
    bag += n // 5   # 최적의 경우
    print(bag)
    break
  n -= 3    # 5를 맞춰주는 과정
  bag += 1  # 3으로만 나눠지는 경우까지 포함

else:   # 3을 빼다가 5로 안나누어지고 3으로도 안되면 -1
  print(-1)
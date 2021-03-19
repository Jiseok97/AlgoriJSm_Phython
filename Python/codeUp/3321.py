# 토핑 종류 : 3
# 도우 가격: 12  토핑의 가격: 2
# 도우의 칼로리: 200
# 토핑의 칼로리
# 50
# 300
# 100
# (300 + 100 + 200) / 16 = int(37)

# 1달러의 열량의 수 구하기

# 소수점 올림 ceil(i)

# nToping = int(input())
# pdt = list(map(int, input().split()))
# kd = int(input())
# toping = []

# price = pdt[0] + (nToping * pdt[1])
# result = kd
# total = 0
# kal = 0
# if nToping != 0:
#   for _ in range(nToping):
#     toping.append(int(input()))
#   toping.sort(reverse=True)
#   print(toping)
#   kal = toping[0] / price
#   for i in toping:
#     total += i
#     if total / price > kal:
#       result += total
#     kal += i

#   print(int(result/price))

# else:
#   print(result)



if __name__ == '__main__' :
    # 토핑 종류 받는 함수 
    toping_num = int(input())

    # 도우 & 토핑 비용
    cost = list(map(int, input().split()))

    # 도우 & 토핑 칼로리 
    D_kcal = int(input())
    T_kcal = []
    
    # 토핑 칼로리 입력
    for i in range(toping_num) :
        T_kcal.append(int(input()))

    # 토핑 칼로리를 내림차순 정렬
    T_kcal.sort(reverse=True)

    # 도우만 있을 경우 
    res = D_kcal / cost[0]

    # 칼로리가 큰 순으로 비교
    for i in T_kcal :
        cost[0] += cost[1]
        if (D_kcal +  i)/cost[0] > res :
            D_kcal += i
            res = D_kcal/cost[0]
        else :
            break
    print(int(res))
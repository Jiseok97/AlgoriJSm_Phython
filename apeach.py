# page: 323~324
# 문자열 압축

# 입력 예시: "aabbaccc"
# 출력 예시: 7 (1개 단위) -> 2a2ba3c
# 입력 예시: "ababcdcdababcdcd" 
# 출력 예시: 9 (2개 단위) -> 2ababcdcd

# 프로그래머스
# https://programmers.co.kr/learn/courses/10336/lessons/64194

def solution(s):
    answer = len(s)
    
    for x in range(1, len(s) // 2 + 1):
        com = ""
        prev = s[0:x]
        count = 1
        for j in range(x, len(s), x):
            if prev == s[j:j + x]:
                count += 1
            else:
                com += str(count) + prev if count >= 2 else prev
                prev = s[j:j + x]
                count = 1
        com += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(com))
    return answer
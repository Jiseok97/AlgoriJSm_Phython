# page: 323~324
# 문자열 압축

# 입력 예시: "aabbaccc"
# 출력 예시: 7 (1개 단위) -> 2a2ba3c
# 입력 예시: "ababcdcdababcdcd" 
# 출력 예시: 9 (2개 단위) -> 2ababcdcd

# 프로그래머스
# 모법 답안
# https://programmers.co.kr/learn/courses/10336/lessons/64194

def solution(s):
    answer = len(s)
    
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        com = ""
        prev = s[0:step]  # 앞에서부터 step만큼의 문자열 추출
        count = 1

        # 단위(step) 크기 만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
            
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                com += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1
        # 남아 있는 문자열에 대해서 처리
        com += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(com))
    return answer


# 또 다른 풀이

def solution(s):
    if len(s) < 3:  # 굳이 1~2개인 경우에는 어차피 1~2개가 나오므로 바로 반환
        return len(s)
    
    answer = len(s)  # 후보 값
    max_cand = int(len(s)/2)  # int를 씌우면 내림이 됨 and 쪼갤 수 있는 길이
    for interval in range(1, max_cand +1 ):  # +1 은 max_cand까지 돌리기 위해서
        start = interval  # 
        res = []
        pre_s = s[0:interval]
        num = 1
        while True:
            now_s = s[start:start+interval]
            if now_s == pre_s:
                num += 1
            else:
                res.append([num.pre_s])
                num = 1
                pre_s = now_s
            
            if start > len(s):
                break
            start += interval
        len_cand = 0 
        for k in range(len(res)):
            if res[k][0] == 1:
                len_cand += len(res[k][1])
            else:
                len_cand += 1
                len_cand += len(res[k][1])
        answer = min(answer, len_cand)

    return answer
import sys
N = int(sys.stdin.readline())
total_num = int(sys.stdin.readline())
num = list(sys.stdin.readline().split())

cand = {}

for i in range(total_num):
    #현재 게시된 사진일 경우
    if cand.get(num[i]): 
        cand[num[i]] += 1
    else:
        #비어있는 사진틀이 없는 경우
        if len(cand) == N:
            min_value = total_num
            for key in reversed(cand.keys()):
                if min_value >= cand[key]:
                    min_value = cand[key]
                    min_key = key    
            #가장 오래된 값 삭제
            cand.pop(min_key)
            #새로 추가
            cand[num[i]] = 1
        else:
            #비어있는 사진틀이 있는 경우
            cand[num[i]] = 1

sorted_keys = sorted(cand.keys(), key = int)

for key in sorted_keys:
    print(key, end=' ')
print()
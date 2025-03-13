import sys
input = sys.stdin.readline

N = int(input())
num = int(input())
recommend = list(map(int, input().split()))

cand = {}

for i in range(num):
    # 이미 게시된 사진일 경우 횟수 증가
    if cand.get(recommend[i]):
        cand[recommend[i]] += 1
    # 아직 게시 안됨
    else:
        # 게시 안됐는데 자리 없을 경우
        if len(cand) == N:
            # 추천 횟수 적은 게 2명 이상일 경우
            min_value = 1000
            for key in reversed(cand.keys()):
                if cand[key] <= min_value:
                    min_value = cand[key]
                    min_key = key
            cand.pop(min_key)       
            cand[recommend[i]] = 1
        else:
            cand[recommend[i]] = 1

# for i in sorted(cand.keys()):
#     print(i, end = ' ')        
    
print(' '.join(map(str, sorted(cand.keys()))))   
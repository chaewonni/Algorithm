import sys
input = sys.stdin.readline

N = int(input())
mm = []

for _ in range(N):
    mm.append(list(input().split()))

mm.sort(key=lambda x: x[1], reverse=True)
mm.sort(key=lambda x: x[0])

for mento, menti in mm:
    print(mento, menti)


#리스트 컴프리헨션..?
#lambda식
# mm = [tuple(input.split()) for _ in range(N)]
# mm.sort(key=lambda x: x[1], reverse=True)
# mm.sort(key=lambda x: x[0])
# res = [' '.join(pair) for pair in mm]
# print('\n'.join(res))

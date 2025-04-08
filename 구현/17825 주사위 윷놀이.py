import sys
input = sys.stdin.readline

# 처음에는 시작 칸에 말 4개
# 파란색 칸에서 이동 시작 -> 파란색 화살표
# 이동하는 도중 or 파란색 아닌 칸에서 이동 시작 -> 빨간색 화살표
# 말 도착 -> 주사위 나온 수와 관계 없이 이동 마침

# 10개턴, 5면체 주사위
# 도착 칸에 있지 않은 말 하나 골라 주사위에 나온 수만큼 이동
# 말이 이동 마치는 칸에 다른 말 있으면 그 말 고를 수 X
# but 이동 마치는 칸이 도착 칸이면 고를 수 O
# 말 이동 마칠 떄마다 칸에 적혀있는 수가 점수에 추가됨

dice = list(map(int, input().split()))
answer = 0
# 아무리 봐도 백트래킹 문제 같은데.. 문제는 이걸 어케 구현하냐..
# 게임판 정의 (graph[i] = [다음칸 번호]) 다음 칸 위치!!!
graph = [[1], [2], [3], [4], [5],
         [6, 21], [7], [8], [9], [10],
         [11, 25], [12], [13], [14], [15],
         [16, 27], [17], [18], [19], [20],
         [32], [22], [23], [24], [30],
         [26], [24], [28], [29], [24],
         [31], [20], [32]]

# 점수 정의
score_list = [0,2,4,6,8,
         10,12,14,16,18,
         20,22,24,26,28,
         30,32,34,36,38,
         40,13,16,19,25,
         22,24,28,27,26,
         30,35,0]

# dfs 안에 for문으로 4개 (말이 4개니까)
# dfs 백트래킹
# turn: 현재까지 몇 턴, start_idx: 말의 위치 (배열), 점수
def dfs(turn, start_idx, score):
    global answer
    
    if turn == 10:
        answer = max(answer, score)
        return
    
    num = dice[turn] # 주사위 몇 나왔는지
            
    for i in range(4):
        horse_idx = start_idx[i] # 현재 말 i의 위치 
        # 이미 도착한 말은 이동 못함
        if horse_idx == 32:
            continue
        
        # 백트래킹을 위해 원래 위치 저장
        origin = horse_idx
        
        # 첫 이동
        if len(graph[horse_idx]) > 1: # 현재 말 i의 위치(시작점)가 파란색이면
            horse_idx = graph[horse_idx][1]  # 파란색 화살표로 가야함
        else: # 아니면
            horse_idx = graph[horse_idx][0] # 빨간색 화살표
            
        # 나머지 이동 (첫 이동은 위에서 했고 num -1 만큼 이동을 해야하니)
        for _ in range(1, num):
            # 도착 칸에 도착한 순간 남은 주사위 수는 무시하고 말의 위치는 32
            if horse_idx == 32: 
                break
            horse_idx = graph[horse_idx][0]
        
        # 겹치는지 확인
        if horse_idx != 32 and horse_idx in start_idx:
            continue # 이 말은 안되니까 다음 말로 넘어감
        
        start_idx[i] = horse_idx
        dfs(turn + 1, start_idx, score + score_list[horse_idx])
        start_idx[i] = origin # 백트래킹 (원상복구) dfs 절에 없는 것만 원상복구 시켜주면됨
    
dfs(0, [0, 0, 0, 0], 0)
print(answer)
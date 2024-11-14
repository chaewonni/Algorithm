import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    queue = deque()
    
    for i in range(len(progresses)):
        queue.append(math.ceil((100-progresses[i])/speeds[i]))
    
    while queue:
        cnt = 0
        fast = queue[0]
        while queue and queue[0]  <= fast:
            queue.popleft()
            cnt += 1
        answer.append(cnt)
    return answer
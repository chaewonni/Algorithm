from collections import deque

def solution(cards1, cards2, goal):
    answer = ''
    queue = deque(goal)
    queue1 = deque(cards1)
    queue2 = deque(cards2)
    
    while queue:
        if queue1 and queue[0] == queue1[0]:
            queue.popleft()
            queue1.popleft()
        elif queue2 and queue[0] == queue2[0]:
            queue.popleft()
            queue2.popleft()
        else:
            answer = "No"
            break
    else:
        answer = "Yes"    
    return answer
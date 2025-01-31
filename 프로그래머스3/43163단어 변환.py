from collections import deque
def solution(begin, target, words):
    answer = 0
    visited = [False] * len(words)
    
    def bfs():
        nonlocal target
        depth = 0
        cnt = 0
        queue = deque([(begin, target, depth)])
        while queue:
            cnt_word, target, depth = queue.popleft()
            if cnt_word == target:
                return depth
            for i, word in enumerate(words):
                diff = 0
                if not visited[i]:
                    # 한 글자만 다른지 확인
                    for j in range(len(word)):
                        if cnt_word[j] != word[j]:
                            diff += 1
                    if diff == 1:
                        visited[i] = True
                        queue.append((word, target, depth + 1))
        else:
            return 0
    answer = bfs()                
    return answer
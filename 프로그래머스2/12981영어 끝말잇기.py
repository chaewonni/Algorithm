def solution(n, words):
    answer = []
    visited = []
    num = 0
    turn = 0

    for i, word in enumerate(words):
        if word not in visited:
            if not visited:
                visited.append(word)
            elif visited[-1][-1] == word[0]:
                visited.append(word)
            else:
                num = i % n + 1
                turn = i // n + 1
                break
                
        else:
            num = i % n + 1
            turn = i // n + 1
            break
    
    answer.append(num)
    answer.append(turn)
    return answer
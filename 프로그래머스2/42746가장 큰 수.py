from functools import cmp_to_key

def solution(numbers):
    
    def compare(x,y):
        if x+y > y+x:
            return -1
        elif x+y < y+x:
            return 1
        else:
            return 0
        
    answer = ''
    numbers = list(map(str, numbers))
    sorted_num = sorted(numbers, key=cmp_to_key(compare))
    answer = ''.join(map(str, sorted_num))
    
    if answer.count('0') == len(answer):
        answer = '0'
        
    return answer
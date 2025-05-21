import sys
input = sys.stdin.readline

T = int(input())

op = ['+', '-']

# 몇까지 쓸 수 있는지, 지금 라운드의 숫자, 현재까지의 숫자들 (3, 2, 1+2)
def dfs(num, cur, total): 
    if len(total) == num * 2 - 1:
        new_total = total.replace(" ", "")
        
        nums = ''
        for i in range(0, len(new_total)):
            if new_total[i] in op:
                break
            nums += new_total[i]
        
        nums = int(nums)

        idx = 0

        # 1-23+4+5+6+7
        while (idx < len(new_total)):
            if new_total[idx] not in op:
                idx += 1
                continue
            
            add = ''
            if new_total[idx] == '+':
                idx += 1
                while (idx < len(new_total) and new_total[idx] not in op):
                    add += new_total[idx]
                    idx += 1

                nums += int(add)
            
            elif new_total[idx] == '-':
                idx += 1
                while (idx < len(new_total) and new_total[idx] not in op):
                    add += new_total[idx]
                    idx += 1
                
                nums -= int(add)

        if nums == 0:
            result.append(total)
            

    if cur < num:
        dfs(num , cur + 1, total + ' ' + str(cur + 1))

        dfs(num, cur + 1, total + '+' + str(cur + 1))

        dfs(num, cur + 1, total + '-' + str(cur + 1))



for _ in range(T):
    N = int(input())

    result = []
    dfs(N, 1,'1')

    for r in result:
        print(r)

    print()
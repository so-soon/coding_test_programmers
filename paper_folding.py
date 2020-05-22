def dfs(depth,num,ans):
    if depth >= folding_num:
        ans.append(num)
        return
    else:
        dfs(depth+1,0,ans)
        ans.append(num)
        dfs(depth+1,1,ans)


def solution(n):
    global folding_num
    folding_num = n
    answer = []

    dfs(1,0,answer)
    return answer

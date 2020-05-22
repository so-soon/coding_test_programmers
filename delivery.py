from _collections import defaultdict,deque

def solution(N, road, K):
    answer = 1

    cost = defaultdict(lambda: [123456789for _ in range(N+1)])
    connection_list = [[] for _ in range(N+1)]
    table = [123456789 for _ in range(N+1)]
    need_to_check = deque()
    answer_set = set()
    for r in road:
        if cost[r[0]][r[1]] == 123456789 : connection_list[r[0]].append(r[1])
        if cost[r[1]][r[0]] == 123456789 : connection_list[r[1]].append(r[0])
        cost[r[0]][r[1]] = min(r[2],cost[r[0]][r[1]])
        cost[r[1]][r[0]] = min(r[2],cost[r[1]][r[0]])

    for i in connection_list[1]:
        need_to_check.append(i)
        table[i] = cost[1][i]
        if table[i] <= K:
            if i not in answer_set:
                answer += 1
                answer_set.add(i)


    answer_set.add(1)

    while len(need_to_check) != 0 :
        check = need_to_check.popleft()
        for i in connection_list[check]:
            if table[i] > table[check] + cost[check][i]: # update
                table[i] = table[check] + cost[check][i]
                need_to_check.append(i)

                if table[i]<=K:
                    if i not in answer_set:
                        answer += 1
                        answer_set.add(i)



    return answer

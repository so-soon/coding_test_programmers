
visit = []
res = []
def solution(begin, target, words):
    answer = 0

    co = 0
    for i in range(len(words)):
        visit.append(0)


    def dfs(word,depth):
        if word == target:
            res.append(depth)
            return
        else:
            for i in range(len(words)):
                if visit[i] == 1:
                    continue

                co = 0
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        co += 1
                if co == 1:
                    visit[i] = 1
                    dfs(words[i],depth+1)
                    visit[i] = 0

    dfs(begin,0)
    if len(res) != 0 :
        answer = min(res)
    return answer

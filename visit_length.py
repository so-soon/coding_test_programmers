from _collections import defaultdict

def solution(skill, skill_trees):
    answer = 0




    for i in range(len(skill_trees)):
        isAvailable = True
        check = defaultdict(lambda: ['0', '0'])
        for j in range(1, len(skill) - 1):
            check[skill[j]] = [skill[j - 1], skill[j + 1]]

        if len(skill) > 1:
            check[skill[0]] = ['s', skill[1]]
            check[skill[-1]] = [skill[-2], '0']

        for c in skill_trees[i]:
            if check[c][0] == '0':
                continue
            else:
                if check[c][0] == 's':
                    check[check[c][1]][0] = 's'
                else:
                    isAvailable = False
                    break
        if isAvailable:
            answer += 1


    return answer

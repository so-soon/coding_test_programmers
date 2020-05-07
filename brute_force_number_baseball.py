from itertools import permutations

def solution(baseball):
    answer = 0
    res = []
    num = ['1','2','3','4','5','6','7','8','9']
    permute  = permutations(num,3)
    for n in permute:

        isCorrect = True
        for q in baseball:
            temp = list(n)
            temp_q = str(q[0])
            co_str = 0
            co_ball = 0
            for i in range(3): # is strike?
                if temp_q[i] == temp[i]:
                    co_str += 1
                    temp[i] = '-1'

            if co_str != q[1]:
                isCorrect = False
                break

            for i in range(3):
                if temp[i] == '-1':
                    continue
                if temp[i] == temp_q[(i+1)%3] or temp[i] == temp_q[(i+2)%3]:
                    co_ball += 1

            if co_ball != q[2]:
                isCorrect = False
                break

        if not isCorrect:
            continue
        else:
            res.append(n)




    answer = len(res)
    return answer

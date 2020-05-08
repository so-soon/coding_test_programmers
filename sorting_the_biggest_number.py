from functools import cmp_to_key
def compare(x,y):
    t1 = int(x+y)
    t2 = int(y+x)

    if t1 > t2:
        return -1
    elif t1 < t2:
        return 1
    else : return 0



def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])


    numbers.sort(key = cmp_to_key(compare))
    answer = ''.join(numbers)
    s = 0
    for i in range(len(answer)):
        if answer[i] == '0':
            s += 1
        else:
            break
    if s != 0:
        answer = answer[s - 1:]

    return answer

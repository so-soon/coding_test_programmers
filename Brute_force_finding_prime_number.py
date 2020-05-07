from itertools import permutations

def isPrime(num):

    i = 2
    while((i*i) <= num):
        if num%i == 0:
            return False
        i += 1
    return True



def solution(numbers):
    answer = 0
    num_list = []
    res = set()
    for i in range(len(numbers)):
        num_list.append(numbers[i])



    for i in range(1,len(numbers)+1):
        permute = permutations(num_list,i)
        for p in permute:
            temp = ""
            for n in p:
                temp+=n
            int_temp = int(temp)
            if int_temp <= 1 :
                continue
            if isPrime(int_temp):
                res.add(int_temp)


    answer = len(res)
    return answer

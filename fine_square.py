import math

def solution(w,h):
    answer = 1
    gcd = math.gcd(w,h)
    answer = w*h - (gcd * ((w//gcd)+(h//gcd)-1))
    return answer

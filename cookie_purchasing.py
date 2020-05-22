def solution(cookie):
    answer = 0

    section_sum = []
    N = len(cookie)
    for i in range(N):
        if i == 0 :
            section_sum.append(cookie[i])
        else:
            section_sum.append(cookie[i]+section_sum[i-1])


    maxi = 0
    isMaxFind = False

    for f in range(0,N):
        for l in range(1,N-f+1):
            if f == 0:
                f_sun = section_sum[f+l-1]
            else:
                f_sun = section_sum[f+l-1] - section_sum[f-1]

            s = f+l
            if f_sun > section_sum[-1] - section_sum[s-1]:
                break
            if f_sun < maxi:
                continue
            for l2 in range(1,N-s+1):
                s_sun = section_sum[s+l2-1] - section_sum[s-1]

                if f_sun == s_sun:
                    maxi = max(maxi,f_sun)
                    if maxi == section_sum[-1]//2:
                        isMaxFind = True
                    break
                    
                elif f_sun < s_sun:
                    break
            if isMaxFind:
                break
        if isMaxFind:
            break

    answer = maxi

    return answer

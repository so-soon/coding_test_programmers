def solution(n, stations, w):
    ans = 0

    cover = (w*2)+1

    for i in range(len(stations)):
        if i == 0:
            if (stations[i]-w-1) <= 0:
                std = -1
            else : std = stations[i]-w-1
        else:
            std = (stations[i]-w) - (stations[i-1]+w) - 1

        if std > 0:
            if std % cover != 0:
                ans += (std // cover) + 1
            else:
                ans += (std // cover)



        if i == len(stations)-1:
            if (n - (stations[i]+w)) <= 0:
                continue
            else: std = (n - (stations[i]+w))

            if std > 0:
                if std % cover != 0:
                    ans += (std // cover) + 1
                else:
                    ans += (std // cover)





    return ans

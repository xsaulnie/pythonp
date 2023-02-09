import sys
import time
import os

def ft_progress(list):
    percent = 0
    lenp = len(list)
    arrow = 0
    sec = time.time()
    eta = 0

    for i in list:

        arrow = ""
        percent = round(i / lenp * 100)
        arrown = round(i / lenp * 20)
        now = time.time() - sec
        eta = (now / (i + 1)) * lenp
        for j in range(arrown - 1):
            arrow += "="
        arrow += ">"
        print("ETA: %.2fs [%3d%%] [%-20s] %d/%d | elapsed time %.2f" % (eta, percent, arrow, i + 1, lenp, now))
        yield i


#listy = range(1000)
#ret = 0
#for elem in ft_progress(listy):
#    ret += (elem + 3) % 5
#    time.sleep(0.01)
#    print()
#    print(ret)

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
    print()
    print(ret)

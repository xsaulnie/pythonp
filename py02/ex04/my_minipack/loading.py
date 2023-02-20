import sys
import time
import os

def ft_progress(list):
    percent = 0
    lenp = len(list)
    arrow = 0
    sec = time.time()
    eta = 0
    cmpt = 0

    for i in list:

        arrow = ""
        percent = round((cmpt + 1 )/ lenp * 100)
        arrown = round((cmpt + 1 )/ lenp * 20)
        now = time.time() - sec
        eta = (now / (cmpt + 1)) * lenp
        for j in range(arrown - 1):
            arrow += "="
        arrow += ">"
        print("ETA: %.2fs [%3d%%] [%-20s] %d/%d | elapsed time %.2f" % (eta, percent, arrow, cmpt + 1, lenp, now))
        cmpt += 1
        yield i

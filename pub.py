
import time
start_time = time.time()
for a in range(1,1001):
    for b in range(0,1001-a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a,b,c:%d,%d,%d" % (a,b,c))
end_start = time.time()
print("运行时间为：%f" %(end_start - start_time))
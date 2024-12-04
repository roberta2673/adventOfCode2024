import subprocess
import time

startTime = time.time()
for day in range(1,26):
    day  = ("0"+str(day))[-2:]
    print("*"*120)
    print("*"*56,"DAY",day,"*"*56)
    print("*"*120)
    res = subprocess.run(f"py day{day}script.py")
    if res.check_returncode():
        exit()
print("*"*120)
print("*"*120)
print("Time:", time.time()-startTime)

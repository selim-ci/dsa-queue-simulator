import random
import time
import os

# make some cars randomly
lns = ['AL2', 'BL2', 'CL2', 'DL2']
fls = ['a.txt', 'b.txt', 'c.txt', 'd.txt']

cid = 1


def mk_car(f, ln):
    global cid
    dr = 'S' if random.random() > 0.3 else 'L'
    tm = int(time.time())

    # write to file
    with open(f, 'a') as fp:
        fp.write(f"{cid},{ln},{dr},{tm}\n")

    print(f"car {cid} -> {ln} ({dr})")
    cid += 1


# clear files first
for f in fls:
    open(f, 'w').close()

print("generating traffic...")
print("ctrl+c to stop\n")

cyc = 0
while True:
    cyc += 1
    print(f"\n--- cycle {cyc} ---")

    # randomly add cars
    for i in range(4):
        if random.random() < 0.7:
            mk_car(fls[i], lns[i])

    # sometimes more on AL2
    if cyc % 5 == 0:
        print("!! AL2 surge !!")
        for _ in range(3):
            mk_car(fls[0], lns[0])
            time.sleep(0.1)

    time.sleep(2)# works now
# change
# done
# works now
# change
# done
# works now
# change
# done
# works now
# change

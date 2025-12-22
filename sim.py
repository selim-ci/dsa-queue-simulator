import time
import os
from queue_stuff import Q, Car, Ln

# setup lanes
lns = []
lns.append(Ln('AL2', True))  # priority one
lns.append(Ln('BL2'))
lns.append(Ln('CL2'))
lns.append(Ln('DL2'))

fls = ['a.txt', 'b.txt', 'c.txt', 'd.txt']

curr = 0  # which lane now
pr_mode = False  # priority mode or not


# read cars from file
def rd_cars(idx):
    if not os.path.exists(fls[idx]):
        return

    try:
        with open(fls[idx], 'r') as f:
            lins = f.readlines()

        for lin in lins:
            if lin.strip():
                pts = lin.strip().split(',')
                if len(pts) == 4:
                    c = Car(int(pts[0]), pts[1], pts[2])
                    lns[idx].q.put(c)

        # clear file after read
        open(fls[idx], 'w').close()
    except:
        pass


# calculate how many to serve
def calc_serve():
    tot = 0
    cnt = 0

    for i in range(4):
        if pr_mode and lns[i].pr:
            continue
        tot += lns[i].q.sz()
        cnt += 1

    if cnt == 0:
        return 1

    avg = (tot + cnt - 1) // cnt
    return max(1, avg)


# which lane next
def nxt_ln():
    global pr_mode, curr

    # check AL2 first
    al2_sz = lns[0].q.sz()

    if al2_sz > 10:
        pr_mode = True
        print(f"[PRIORITY] AL2 has {al2_sz} cars (>10)")
        return 0

    if pr_mode and al2_sz < 5:
        pr_mode = False
        print(f"[NORMAL] AL2 down to {al2_sz} cars (<5)")

    if pr_mode:
        return 0

    # round robin
    st = curr
    for i in range(4):
        idx = (st + i) % 4
        if not lns[idx].q.empty():
            return idx

    return -1


# show status
def show():
    print("\n" + "=" * 40)
    print("JUNCTION STATUS")
    print("=" * 40)

    for ln in lns:
        sz = ln.q.sz()
        bar = "█" * min(sz, 20) + " " * (20 - min(sz, 20))
        print(f"{ln.nm}: [{bar}] {sz}")

    print("-" * 40)
    print(f"Mode: {'PRIORITY' if pr_mode else 'NORMAL'}")
    print("=" * 40)


# process one cycle
def proc():
    global curr

    idx = nxt_ln()

    if idx == -1:
        print("[idle] no cars waiting")
        return

    ln = lns[idx]

    # how many to serve
    if pr_mode:
        n = ln.q.sz()
    else:
        n = calc_serve()

    n = min(n, ln.q.sz())

    print(f"\n>>> GREEN: {ln.nm}")
    print(f"serving {n} cars")

    # serve cars
    for i in range(n):
        if not ln.q.empty():
            c = ln.q.get()
            print(f"  car {c.i} from {c.ln} ({c.d}) passed")
            time.sleep(1)

    print(f"remaining in {ln.nm}: {ln.q.sz()}")

    if not pr_mode:
        curr = (idx + 1) % 4


print("=" * 40)
print("TRAFFIC SIMULATOR")
print("=" * 40)
print()

cyc = 0

try:
    while True:
        cyc += 1
        print(f"\n\nCYCLE {cyc}")
        print("-" * 40)

        # read new cars
        for i in range(4):
            rd_cars(i)

        show()
        proc()

        time.sleep(2)

except KeyboardInterrupt:
    print("\n\nstopping...")# edit
# more
# update
# change
# thing
# edit again
# more changes
# test
# edit
# more
# update
# change
# thing
# edit again
# more changes
# test
# edit
# more
# update
# change
# thing
# edit again
# more changes
# test
# edit

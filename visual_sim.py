import pygame
import time
import os
from queue_stuff import Q, Car, Ln

pygame.init()

# screen
w = 1000
h = 800
scr = pygame.display.set_mode((w, h))
pygame.display.set_caption("Traffic Thing")

# colors
wh = (255, 255, 255)
bk = (0, 0, 0)
rd = (255, 0, 0)
gr = (0, 255, 0)
bl = (100, 149, 237)
gy = (50, 50, 50)

fnt = pygame.font.Font(None, 30)
sf = pygame.font.Font(None, 24)

# lanes
lns = []
lns.append(Ln('AL2', True))
lns.append(Ln('BL2'))
lns.append(Ln('CL2'))
lns.append(Ln('DL2'))

fls = ['a.txt', 'b.txt', 'c.txt', 'd.txt']

c = 0
pm = False
gl = -1
lt = time.time()

def rd_cars(idx):
    if not os.path.exists(fls[idx]):
        return
    try:
        with open(fls[idx], 'r') as f:
            ls = f.readlines()
        for l in ls:
            if l.strip():
                p = l.strip().split(',')
                if len(p) == 4:
                    cr = Car(int(p[0]), p[1], p[2])
                    lns[idx].q.put(cr)
        open(fls[idx], 'w').close()
    except:
        pass

def calc():
    t = 0
    ct = 0
    for i in range(4):
        if pm and lns[i].pr:
            continue
        t += lns[i].q.sz()
        ct += 1
    if ct == 0:
        return 1
    a = (t + ct - 1) // ct
    return max(1, a)

def nxt():
    global pm, c
    s = lns[0].q.sz()
    if s > 10:
        pm = True
        return 0
    if pm and s < 5:
        pm = False
    if pm:
        return 0
    st = c
    for i in range(4):
        idx = (st + i) % 4
        if not lns[idx].q.empty():
            return idx
    return -1

def drw():
    scr.fill(wh)
    
    # title
    tt = fnt.render("TRAFFIC SIMULATOR", True, bk)
    scr.blit(tt, (w//2 - tt.get_width()//2, 20))
    
    # mode
    mt = f"Mode: {'PRIORITY' if pm else 'NORMAL'}"
    m = sf.render(mt, True, rd if pm else gr)
    scr.blit(m, (w//2 - m.get_width()//2, 60))
    
    # intersection box
    pygame.draw.rect(scr, gy, (w//2 - 80, h//2 - 80, 160, 160))
    
    # lane pos
    pos = [
        (w//2 - 40, 150),
        (750, h//2 - 40),
        (w//2 - 40, 580),
        (150, h//2 - 40)
    ]
    
    for i, ln in enumerate(lns):
        x, y = pos[i]
        
        # name
        n = sf.render(ln.nm, True, bk)
        if i == 0:
            scr.blit(n, (x, y - 30))
        elif i == 1:
            scr.blit(n, (x + 100, y))
        elif i == 2:
            scr.blit(n, (x, y + 100))
        else:
            scr.blit(n, (x - 100, y))
        
        # light
        lc = gr if gl == i else rd
        if i == 0:
            pygame.draw.circle(scr, lc, (x + 40, y + 100), 15)
        elif i == 1:
            pygame.draw.circle(scr, lc, (x - 20, y + 40), 15)
        elif i == 2:
            pygame.draw.circle(scr, lc, (x + 40, y - 20), 15)
        else:
            pygame.draw.circle(scr, lc, (x + 100, y + 40), 15)
        
        # count
        qs = ln.q.sz()
        ct = f"Cars: {qs}"
        co = sf.render(ct, True, bk)
        
        if i == 0:
            scr.blit(co, (x, y - 50))
            for j in range(min(qs, 8)):
                cy = y - 80 - (j * 25)
                pygame.draw.rect(scr, bl, (x + 10, cy, 60, 20))
        elif i == 1:
            scr.blit(co, (x + 100, y - 30))
            for j in range(min(qs, 8)):
                cx = x + 120 + (j * 25)
                pygame.draw.rect(scr, bl, (cx, y + 10, 20, 60))
        elif i == 2:
            scr.blit(co, (x, y + 120))
            for j in range(min(qs, 8)):
                cy = y + 140 + (j * 25)
                pygame.draw.rect(scr, bl, (x + 10, cy, 60, 20))
        else:
            scr.blit(co, (x - 100, y - 30))
            for j in range(min(qs, 8)):
                cx = x - 140 - (j * 25)
                pygame.draw.rect(scr, bl, (cx, y + 10, 20, 60))
        
        if ln.pr:
            pt = sf.render("PRIORITY", True, rd)
            scr.blit(pt, (x - 20, y - 70))
    
    pygame.display.flip()

def proc():
    global c, gl
    idx = nxt()
    if idx == -1:
        gl = -1
        return
    gl = idx
    ln = lns[idx]
    if pm:
        n = min(3, ln.q.sz())
    else:
        n = min(calc(), ln.q.sz())
    for i in range(n):
        if not ln.q.empty():
            cr = ln.q.get()
            time.sleep(0.3)
            drw()
    if not pm:
        c = (idx + 1) % 4

run = True
clk = pygame.time.Clock()

print("starting visual thing")

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    
    if time.time() - lt > 2:
        for i in range(4):
            rd_cars(i)
        proc()
        lt = time.time()
    
    drw()
    clk.tick(30)

pygame.quit()
print("done")

# Assignment 1 Report

**Name:** Shaikh Abdullah Nepal 
**Roll Number:** 46 
**Course:** COMP202 - Data Structure and Algorithms

---

## Summary of Work

implemented traffic light simulation system using queue data structure. made 3 python files that work together - one generates cars randomly, one has queue implementation, and main visual simulator with pygame that shows animated traffic junction.

system reads car data from text files and manages 4 lanes with different priorities. normal mode uses round robin but switches to priority mode automatically based on AL2 queue size. visual interface shows traffic lights changing color and cars moving through junction in real time.

---

## Data Structure Used

| Data Structure | Implementation | Purpose |
|---|---|---|
| Queue (FIFO) | Python list with index tracking | store cars waiting in each lane |
| Car object | Python class with attributes | represent individual vehicle with id, lane, direction |
| Lane object | Python class with queue | manage each lane properties and car queue |

### Queue Implementation Details

used list-based implementation where:
- `put()` appends to end of list
- `get()` removes from front using pop(0)
- maintains FIFO order
- dynamic size (list grows automatically)

---

## Functions Implemented

### queue_stuff.py
- `Q.__init__()` - initialize empty queue
- `Q.put(x)` - add item to queue
- `Q.get()` - remove and return front item
- `Q.sz()` - return queue size
- `Q.empty()` - check if queue empty
- `Car.__init__()` - create car object
- `Ln.__init__()` - create lane with queue

### gen_cars.py
- `mk_car(f, ln)` - generate random car and write to file

### visual_sim.py
- `rd_cars(idx)` - read cars from file into queue
- `calc()` - calculate average cars to serve
- `nxt()` - determine next lane to serve
- `drw()` - render visual interface with pygame showing traffic lights and cars
- `proc()` - process one traffic light cycle and update display

---

## Algorithm

### Main Algorithm Logic

```
initialize pygame window
initialize 4 lanes with queues
set AL2 as priority lane
priority_mode = false
current_lane = 0

while window open:
    // read new cars every 2 seconds
    for each lane:
        read cars from file
        add to lane queue
    
    // check priority condition
    if AL2.size > 10:
        priority_mode = true
        serve AL2
    else if priority_mode and AL2.size < 5:
        priority_mode = false
    
    // determine cars to serve
    if priority_mode:
        cars_to_serve = min(3, AL2.size)
    else:
        cars_to_serve = average(all_lanes)
    
    // serve cars with animation
    set traffic light to green for current lane
    for i in cars_to_serve:
        dequeue from current lane
        update visual display
        wait 0.3 seconds
    
    // next lane
    if not priority_mode:
        current_lane = (current_lane + 1) % 4
    
    render display at 30 FPS
```

### Priority Detection Algorithm

```
check AL2 queue size
if size > 10:
    enter priority mode
    serve only AL2
    
while in priority mode:
    serve AL2 cars
    if AL2.size < 5:
        exit priority mode
        resume normal operation
```

### Average Calculation

```
total = 0
count = 0

for each normal lane:
    total += lane.queue.size
    count += 1

average = ceiling(total / count)
serve min(average, current_lane.size) cars
```

### Visualization

uses pygame to display:
- traffic lights (red/green circles) for each lane
- blue rectangles representing waiting cars
- lane names and car counts
- priority mode indicator
- real-time updates at 30 FPS

---

## Time Complexity Analysis

### Individual Operations

**Queue Operations:**
- Enqueue (put): **O(1)** - appending to list is constant time
- Dequeue (get): **O(n)** - pop(0) requires shifting elements, where n is queue size
- Size check: **O(1)** - len() is constant time
- Empty check: **O(1)** - comparison is constant time

**Lane Operations:**
- Read cars from file: **O(k)** - where k is number of cars in file
- Add to queue: **O(1)** per car

**Traffic Processing:**
- Check priority: **O(1)** - simple comparison
- Calculate average: **O(4)** = **O(1)** - fixed 4 lanes
- Serve cars: **O(m × n)** - where m is cars served, n is queue size for dequeue operation

**Visualization:**
- Render display: **O(v)** - where v is number of visual elements (constant)
- Update screen: **O(1)** - pygame flip operation

### Overall Complexity Per Cycle

```
Read phase: O(k) where k = total new cars
Process phase: O(1) priority check + O(1) average calc + O(m × n) serve cars
Render phase: O(v) where v is constant visual elements
Total: O(k + m × n + v) ≈ O(m × n)
```

In practical terms:
- k is typically small (few cars per cycle)
- m is bounded by average queue size (usually <10)
- n is queue size (typically <20)
- v is constant (fixed UI elements)

**Overall complexity per cycle: O(n²)** in worst case, but **O(n)** in average case due to small queue sizes.

### Optimization Notes

current implementation uses `pop(0)` which is O(n). could optimize to O(1) by using `collections.deque` but not done for simplicity and queue sizes are small so performance impact minimal.

pygame rendering is efficient enough for this application with 30 FPS update rate.

---

## Source Code

GitHub Repository: https://github.com/selim-ci/dsa-queue-simulator.git

Files:
- queue_stuff.py - queue implementation
- gen_cars.py - car generator
- visual_sim.py - animated visual simulator with pygame
- README.md - documentation

---

## Testing

tested with:
- normal traffic flow
- AL2 surge conditions (>10 cars)
- empty lanes
- all lanes with cars
- priority mode transition
- visual display and animation working correctly

all scenarios work as expected based on assignment requirements. visualization clearly shows traffic lights changing and cars moving through junction.

Video 
 https://github.com/user-attachments/assets/e4138bd9-c3b2-46ca-87c1-4c83d7151e44 https://github.com/user-attachments/assets/9ba9177a-c821-4836-91e4-a39cf49f1f21

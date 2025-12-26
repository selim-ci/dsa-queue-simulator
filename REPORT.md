# Assignment 1 Report

**Name:** Shaikh Abdullah Nepal 
**Roll Number:** 46  
**Course:** COMP202 - Data Structure and Algorithms

---

## Summary of Work

implemented traffic light simulation system using queue data structure. made 3 python files that work together - one generates cars randomly, one has queue implementation, and main simulator processes everything. AL2 lane becomes priority when more than 10 cars waiting.

system reads car data from text files and manages 4 lanes with different priorities. normal mode uses round robin but switches to priority mode automatically based on AL2 queue size.

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

### sim.py
- `rd_cars(idx)` - read cars from file into queue
- `calc_serve()` - calculate average cars to serve
- `nxt_ln()` - determine next lane to serve
- `show()` - display current junction status
- `proc()` - process one traffic light cycle

---

## Algorithm

### Main Algorithm Logic
```
initialize 4 lanes with queues
set AL2 as priority lane
priority_mode = false
current_lane = 0

while running:
    // read new cars
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
        cars_to_serve = AL2.size
    else:
        cars_to_serve = average(all_lanes)
    
    // serve cars
    for i in cars_to_serve:
        dequeue from current lane
        simulate passing
    
    // next lane
    if not priority_mode:
        current_lane = (current_lane + 1) % 4
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

### Overall Complexity Per Cycle
```
Read phase: O(k) where k = total new cars
Process phase: O(1) priority check + O(1) average calc + O(m × n) serve cars
Total: O(k + m × n)
```

In practical terms:
- k is typically small (few cars per cycle)
- m is bounded by average queue size (usually <10)
- n is queue size (typically <20)

**Overall complexity per cycle: O(n²)** in worst case, but **O(n)** in average case due to small queue sizes.

### Optimization Notes

current implementation uses `pop(0)` which is O(n). could optimize to O(1) by using `collections.deque` but not done for simplicity and queue sizes are small so performance impact minimal.

---

## Source Code

GitHub Repository: https://github.com/selim-ci/dsa-queue-simulator.git

Files:
- queue_stuff.py - queue implementation
- gen_cars.py - car generator
- sim.py - main simulator
- README.md - documentation

---

## Testing

tested with:
- normal traffic flow
- AL2 surge conditions (>10 cars)
- empty lanes
- all lanes with cars
- priority mode transition

all scenarios work as expected based on assignment requirements.
# final
# final
# final

# Traffic Queue Simulator

implementation of traffic junction with queue for assignment 1

## What it does

manages 4 lanes (AL2, BL2, CL2, DL2) with queue data structure. AL2 is priority lane that gets served first when more than 10 cars waiting. shows animated visual interface with traffic lights and cars.

## Files

- `queue_stuff.py` - has queue class and car/lane classes
- `gen_cars.py` - generates random cars and writes to files
- `visual_sim.py` - animated simulator with pygame showing traffic junction

## Requirements

need python 3 and pygame

install pygame:
```
pip install pygame
```

## How to run

### running both programs

Terminal 1:
```
python gen_cars.py
```

Terminal 2:
```
python visual_sim.py
```

stop with ctrl+c

opens window showing animated traffic junction with lights turning red/green and cars moving through

## Data Structures

### Queue (Q class)
- uses list to store items
- put() adds to end
- get() removes from front
- FIFO structure

### Car class
- stores car id, lane, direction, timestamp

### Lane class  
- has name, queue of cars, priority flag

## Algorithm

1. generator makes random cars every 2 sec
2. writes car data to text files (a.txt, b.txt, c.txt, d.txt)
3. visual simulator reads files each cycle
4. checks if AL2 has >10 cars -> priority mode
5. in priority mode serves AL2 until <5 cars
6. in normal mode calculates average cars in lanes
7. serves that many cars from current lane
8. uses round robin to pick next lane
9. displays everything with pygame - traffic lights, cars, counts

### Time Complexity

- enqueue: O(1)
- dequeue: O(1)  
- checking priority: O(1)
- calculating average: O(n) where n=4 lanes
- serving cars: O(m) where m=cars served
- rendering: O(1) constant visual elements

overall per cycle: O(n + m) = O(1) since n is constant 4

## Output

animated window showing:
- 4 lanes with traffic lights
- blue rectangles = cars waiting
- lights turn green when lane is being served
- car counts for each lane
- priority mode indicator



## references

- used basic python queue implementation
- round robin scheduling concept from OS
- priority queue logic from assignment description
- pygame for visualization

Video
https://github.com/user-attachments/assets/e4138bd9-c3b2-46ca-87c1-4c83d7151e44
https://github.com/user-attachments/assets/9ba9177a-c821-4836-91e4-a39cf49f1f21


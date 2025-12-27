# Traffic Queue Simulator

implementation of traffic junction with queue for assignment 1

## What it does

manages 4 lanes (AL2, BL2, CL2, DL2) with queue data structure. AL2 is priority lane that gets served first when more than 10 cars waiting.

## Files

- `queue_stuff.py` - has queue class and car/lane classes
- `gen_cars.py` - generates random cars and writes to files
- `sim.py` - main simulator that reads cars and processes them

## How to run

need python 3 and pygame

### install pygame
```
pip install pygame
```

### running

Terminal 1:
```
python gen_cars.py
```

Terminal 2:
```
python visual_sim.py
```

Opens animated window showing traffic junction with lights and cars

### running both programs

Terminal 1:
```
python gen_cars.py
```

Terminal 2:
```
python sim.py
```

stop with ctrl+c

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
3. simulator reads files each cycle
4. checks if AL2 has >10 cars -> priority mode
5. in priority mode serves AL2 until <5 cars
6. in normal mode calculates average cars in lanes
7. serves that many cars from current lane
8. uses round robin to pick next lane

### Time Complexity

- enqueue: O(1)
- dequeue: O(1)  
- checking priority: O(1)
- calculating average: O(n) where n=4 lanes
- serving cars: O(m) where m=cars served

overall per cycle: O(n + m) = O(1) since n is constant 4

## Output

shows bar graph of cars waiting in each lane and serves them based on algorithm

## references

- used basic python queue implementation
- round robin scheduling concept from OS
- priority queue logic from assignment description

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Car Fleet: is a nonempty SET of cars driving at SAME (1) position AND (2) speed
        # step 1: lets first frame the problem
            # what is our goal state? What are the constraints? and what do we need to compute to get there?
            # Goal State: return the number of different CarFleets that will arrive at destination (the value in 'target' var)
            # Constraints: A car CANNOT pass another car ahead of it. Can only catch up then drive at SAME SPEED
            # What do I need to Compute: for each car in position, register its distance. If distance is less than
            # max distance seen so far then its worth seeing if it can catch up.
            # register its speed and then also register the speed of the car whose distance was just found to be greater
            # compute meet_distance and if meet_distance < target then current car is added to max_dist_car's CarFleet

            # KEY POINT: if carC which is at pos8 catches up to carB which as at pos4 and carB catches up to 
            # carC which is at pos2 then carC, carB and carA are all in the same carfleet anchored by carA
        # step 2: What is the brute force approach?
            # initialise num_car_fleets to len(positions)
            # combine position and speed into tuples to bundle the information together
            # sort car_info list by position ascending order so car closest to target is last.
            # for each car, record its position and speed, then extract info ONLY for CAR AHEAD
            # check if 2 cars catch up ie find their
            # meet_distance and check if meet_distance <= target. If so, then num_car_fleets decreases by 1.
            # loop through all cars in positions and return num_car_fleets (can be minimum 1).

        # step 3: What is my Invariant and Per-step Rule?
            # Invariant: We process cars from back to front (closest from target to furthest), 
            # the carfleet on top of the stack is the arrival time of the carfleet AHEAD of current car

            # Per-Step Rule: Compute current car's arrival time. If arrival_time is <= arrival_time of carfleet on
            # top of stack then DO NOT PUSH as every car in car fleet travels at speed of car furthest ahead (the fleet's anchor car) which is
            # already on stack!

            # if cars do not meet, then we have a new car fleet anchor so we must PUSH
            
            # num_car_fleets = len(stack) at end of loop!

        car_info = []
        for i in range(len(position)):
            car_info.append((position[i], speed[i]))
        
        carfleet_stack = [] # the values in this stack are arrival times of each fleet's anchor car
        
        sorted_car_info = sorted(car_info, key= lambda x: x[0], reverse=True) # sort in positional descending order (closest to target first)

        print(sorted_car_info)

        def compute_arrival_time(position, speed):
            nonlocal target
            arrival_time = (target - position) / speed
            return arrival_time

        for car_pos, car_speed in sorted_car_info:
            if not carfleet_stack:
                car_arrival_time = compute_arrival_time(car_pos, car_speed)
                carfleet_stack.append((car_arrival_time))
                continue
            
            car_arrival_time = compute_arrival_time(car_pos, car_speed)
            if car_arrival_time <= carfleet_stack[-1]: # arrival time of current car LESS than fleet ahead therefore current car CATCHES UP
                continue # do NOTHING, it merges into fleet ahead which is represented by the anchor car's arrival time

            carfleet_stack.append(car_arrival_time) # car DOES NOT catch up therefore PUSH TO STACK as we have a new fleet with new anchor car (and arrival_time)
        
        return len(carfleet_stack)
         
            
            








"""
The main file for controlling the entire project

Pseudo code
------------

Setup LOOP:
- calibrate
- if calibrated move on to normal loop

Normal LOOP:
- load models
- START LOOP
    - capture frames 
    - create thread for iris, returns grid location
    - create thread for gesture, returns gesture
    - wait for both threads to join
    - decision making with both inputs
    - run appropriate decision with actuator

"""
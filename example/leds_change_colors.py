
from adafruit_circuitplayground import cp
import time
from state_machine import StateMachine
from timer_collection import TimerCollection

timer_collection = TimerCollection()

def change_state():
    print("i'm working")
    for pixel in range(10):
        if(sm.get_state() == 'blue'):
            cp.pixels[pixel] = blue
        else:
            cp.pixels[pixel] = red

    acceleration_factor = abs(cp.acceleration.z - 10) * 0.05
    print(acceleration_factor)

    if(acceleration_factor > 0.1):
        sm.handle_event('change to red')
    else:
        sm.handle_event('change to blue')

timer_collection.start_periodic_timer(1, change_state)

cp.pixels.brightness = 0.01
blue = (0, 0, 255)
red = (255, 0, 0)

sm = StateMachine('blue')

sm.add_transition('change to red', 'red')
sm.add_transition('change to blue', 'blue')

while True:
    time_until_next = timer_collection.run()

    if time_until_next != None:
        time.sleep(time_until_next)
    else:
        time.sleep(1)

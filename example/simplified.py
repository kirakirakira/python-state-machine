# Define signal values
SIGNAL_ENTRY = 0
SIGNAL_EXIT = 1
SIGNAL_USER_START = 2

class fsm:
    def __init__(self, current = None):
        self.current = current

    # Initializes an FSM with the specified initial state. Sends the entry signal to the
    # initial state.
    def init(self, initial):
        self.current = initial
        self.current(self, SIGNAL_ENTRY, None)

    # Sends a signal and optional signal data to the current state.
    def send_signal(self, signal, data):
        self.current(self, signal, data)

    # Transitions the FSM to the target state. Sends exit to the current state, changes
    # state, then sends entry to the target state.
    def transition(self, target):
        self.current(self, SIGNAL_EXIT, None)
        self.current = target
        self.current(self, SIGNAL_ENTRY, None)


from adafruit_circuitplayground import cp
import time

# Define the possible states
def led_off_state(fsm: fsm, signal, data):
    if signal == SIGNAL_ENTRY:
        print("i am in the off state")
        cp.red_led = False
    elif signal == SIGNAL_USER_START:
        fsm.transition(led_on_state)

def led_on_state(fsm: fsm, signal, data):
    if signal == SIGNAL_ENTRY:
        print("i am in the on state")
        cp.red_led = True
    elif signal == SIGNAL_USER_START:
        fsm.transition(led_off_state)

# Create the FSM and initialize it with the initial state
fsm = fsm(current=led_off_state)
fsm.init(led_off_state)

# Loop forever
while True:
    # Send the user start signal to toggle the LED
    fsm.send_signal(SIGNAL_USER_START, None)
    time.sleep(1.5)

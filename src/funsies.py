from typing import Optional

# Define signal values
TINY_FSM_SIGNAL_ENTRY = 0
TINY_FSM_SIGNAL_EXIT = 1
TINY_FSM_SIGNAL_USER_START = 2

# Define the signal type
TINY_FSM_SIGNAL_T = int

# Define the state type
TINY_FSM_STATE_T = Optional["tiny_fsm_t"]


class tiny_fsm_t:
    def __init__(self, current: TINY_FSM_STATE_T = None):
        self.current = current

    # Initializes an FSM with the specified initial state. Sends the entry signal to the
    # initial state.
    def tiny_fsm_init(self, initial: TINY_FSM_STATE_T):
        self.current = initial
        self.current(self, TINY_FSM_SIGNAL_ENTRY, None)

    # Sends a signal and optional signal data to the current state.
    def tiny_fsm_send_signal(self, signal: TINY_FSM_SIGNAL_T, data: Optional[object]):
        self.current(self, signal, data)

    # Transitions the FSM to the target state. Sends exit to the current state, changes
    # state, then sends entry to the target state.
    def tiny_fsm_transition(self, target: TINY_FSM_STATE_T):
        self.current(self, TINY_FSM_SIGNAL_EXIT, None)
        self.current = target
        self.current(self, TINY_FSM_SIGNAL_ENTRY, None)


# Define the state function signature
def tiny_fsm_state_t(fsm: tiny_fsm_t, signal: TINY_FSM_SIGNAL_T, data: Optional[object]):
    pass


import board
import time

# Define the LED pin
LED_PIN = board.D13

# Define the possible states
def led_off_state(fsm: tiny_fsm_t, signal: TINY_FSM_SIGNAL_T, data: Optional[object]):
    if signal == TINY_FSM_SIGNAL_ENTRY:
        board.digitalio.DigitalInOut(LED_PIN).direction = board.Direction.OUTPUT
        board.digitalio.DigitalInOut(LED_PIN).value = False
    elif signal == TINY_FSM_SIGNAL_USER_START:
        fsm.tiny_fsm_transition(led_on_state)

def led_on_state(fsm: tiny_fsm_t, signal: TINY_FSM_SIGNAL_T, data: Optional[object]):
    if signal == TINY_FSM_SIGNAL_ENTRY:
        board.digitalio.DigitalInOut(LED_PIN).value = True
    elif signal == TINY_FSM_SIGNAL_USER_START:
        fsm.tiny_fsm_transition(led_off_state)

# Create the FSM and initialize it with the initial state
fsm = tiny_fsm_t(current=led_off_state)
fsm.tiny_fsm_init(led_off_state)

# Loop forever
while True:
    # Send the user start signal to toggle the LED
    fsm.tiny_fsm_send_signal(TINY_FSM_SIGNAL_USER_START, None)
    time.sleep(1.0)


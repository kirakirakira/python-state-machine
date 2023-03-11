# Define signal values
SIGNAL_ENTRY = 0
SIGNAL_EXIT = 1
SIGNAL_USER_START = 2

class fsm:
    def __init__(self, initial):
        self.current = initial(self, SIGNAL_ENTRY, None)

    # # Initializes an FSM with the specified initial state. Sends the entry signal to the
    # # initial state.
    # def init(self, initial):
    #     self.current = initial

    # Sends a signal and optional signal data to the current state.
    def send_signal(self, signal, data):
        self.current(self, signal, data)

    # Transitions the FSM to the target state. Sends exit to the current state, changes
    # state, then sends entry to the target state.
    def transition(self, target):
        self.current(self, SIGNAL_EXIT, None)
        self.current = target(self, SIGNAL_ENTRY, None)

class StateMachine:
    def __init__(self, initial_state):
        self.current_state = initial_state
        self.transitions = {}

    def add_transition(self, event, next_state):
        self.transitions[event] = next_state

    def handle_event(self, event):
        next_state = self.transitions.get(event, None)
        if next_state is not None:
            self.current_state = next_state

    def get_state(self):
        return self.current_state

sm = StateMachine('off')
sm.add_transition('start', 'on')
sm.add_transition('process', 'processing')
sm.add_transition('finish', 'off')
sm.add_transition('error', 'error')

print(sm.get_state())
# Output: off

sm.handle_event('start')
print(sm.get_state())
# Output: on

sm.handle_event('process')
print(sm.get_state())
# Output: processing

sm.handle_event('finish')
print(sm.get_state())
# Output: off

sm.handle_event('error')
print(sm.get_state())
# Output: error

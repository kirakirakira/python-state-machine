from state_machine import fsm, SIGNAL_ENTRY, SIGNAL_EXIT, SIGNAL_USER_START

class MyState:
    def on_entry(self, fsm, signal, data):
        if signal == SIGNAL_ENTRY:
            print("Entering MyState")

    def on_exit(self, fsm, signal, data):
        if signal == SIGNAL_EXIT:
            print("Exiting MyState")

    def on_signal(self, fsm, signal, data):
        if signal == SIGNAL_USER_START:
            print("Received SIGNAL_USER_START with data:", data)

my_state = MyState()
my_fsm = fsm(initial=my_state.on_entry)

my_fsm.send_signal(SIGNAL_USER_START, "some data")

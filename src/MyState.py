from state_machine import fsm, SIGNAL_ENTRY, SIGNAL_EXIT, SIGNAL_USER_START

class MyState:
    def state_A(self, fsm, signal, data):
        if signal == SIGNAL_ENTRY:
            print("Entering MyState")

    def state_B(self, fsm, signal, data):
        print("signal is ", signal)
        if signal == SIGNAL_EXIT:
            print("Exiting MyState")

    def state_C(self, fsm, signal, data):
        if signal == SIGNAL_USER_START:
            print("Received SIGNAL_USER_START with data:", data)

my_state = MyState()
my_fsm = fsm(initial=my_state.state_A)

my_fsm.send_signal(SIGNAL_USER_START, "some data")
my_state.state_B(my_fsm, SIGNAL_EXIT, "whoo")

my_fsm.transition(my_state.state_B, SIGNAL_EXIT)

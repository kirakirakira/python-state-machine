class StateMachine:
    def __init__(self, initialState) -> None:
        self.currentState = initialState
        self.sendSignal("ENTRY", None)

    def transition(self, targetState):
        self.sendSignal("EXIT", None)
        self.currentState = targetState
        self.sendSignal("ENTRY", None)

    def sendSignal(self, signal, data):
        # self.currentState(self, signal, data)
        pass

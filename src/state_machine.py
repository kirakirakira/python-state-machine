class StateMachine:
    def __init__(self, initialState) -> None:
        self.currentState = initialState

    def transition(self, targetState):
        pass

    def sendSignal(self, signal, data):
        pass

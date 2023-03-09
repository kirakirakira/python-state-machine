class StateMachine:
    def __init__(self, initialState) -> None:
        self.currentState = initialState
        self.signals = {}
        # self.sendSignal("ENTRY", None)

    def transition(self, targetState):
        # self.sendSignal("EXIT", None)
        self.currentState = targetState
        # self.sendSignal("ENTRY", None)

    def addSignal(self, targetState, signal):
        if targetState not in self.signals:
            self.signals[targetState] = signal
        else:
            self.signals[targetState].append(signal)
        # self.currentState(self, signal, data)

    def getState(self):
        return self.currentState

    def sendSignal(self, signal):
        for state, signals in self.signals.items():
            if signal in signals:
                print("you got it")


sm = StateMachine("off")
print(sm.getState())

sm.transition("on")
print(sm.getState())

sm.addSignal("off", "go to on")

sm.sendSignal("go to on")

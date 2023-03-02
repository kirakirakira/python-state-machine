import unittest
from src.state_machine import StateMachine
from unittest import mock
from unittest.mock import patch, call

class TestStateMachine(unittest.TestCase):
    def setUp(self):
        pass

    # @patch(__name__ +'.StateMachine')
    def test_init(self, *newargs, **newkeywargs):
        with patch(__name__ + '.StateMachine') as Statey:
            print(Statey)
            expected_calls = [call.sendSignal("ENTRY", None)]
            new_state_machine = StateMachine("running")
            Statey.return_value.assert_has_calls(expected_calls)

    def test_transition(self):
        new_state_machine = StateMachine("running")
        # expect send entry signal
    #     new_state_machine.transition("stopped")
    #     # expect send exit signal of running
    #     # expect send entry signal of stopped

    # def test_send_signal(self):
    #     new_state_machine = StateMachine("running")
    #     # expect send entry signal of running
    #     new_state_machine.sendSignal("turn on led", None)
    #     # expect send turn on led signal

if __name__ == '__main__':
    unittest.main()

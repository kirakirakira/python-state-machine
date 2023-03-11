import unittest
from src.MyState import MyState, SIGNAL_ENTRY, SIGNAL_EXIT, SIGNAL_USER_START
from src.state_machine import fsm
from unittest import mock
from unittest.mock import patch

class testmystate(unittest.TestCase):
    def setUp(self):
        print("set up")
        self.state = MyState()
        self.fsm = fsm(initial=self.state.state_A)

    def test_state_A(self):
        with mock.patch.object(self.state, 'state_A') as mock_state_A:
            self.fsm.transition(self.state.state_A, SIGNAL_ENTRY)
            mock_state_A.assert_called_once_with(self.fsm, SIGNAL_ENTRY, None)

    def test_state_B(self):
        print("starting test")
        # self.state.state_B(self.fsm, SIGNAL_EXIT, "whoo")
        # self.fsm.transition(self.state.state_B, SIGNAL_EXIT)
        # my_state = MyState()

        with mock.patch.object(self.state, 'state_B') as mock_state_B:
            self.fsm.transition(self.state.state_B, SIGNAL_EXIT)
            mock_state_B.assert_has_calls([mock.call(self.fsm, SIGNAL_ENTRY, None)])

        print("finished test")

    # def test_on_signal(self):
    #     with mock.patch.object(self.state, 'on_signal') as mock_on_signal:
    #         self.fsm.send_signal(SIGNAL_USER_START, "some data")
    #         mock_on_signal.assert_called_once_with(self.fsm, SIGNAL_USER_START, "some data")

if __name__ == '__main__':
    unittest.main()

import unittest
from src.state_machine import fsm, SIGNAL_ENTRY, SIGNAL_EXIT, SIGNAL_USER_START
from unittest import mock
from unittest.mock import patch, call

# def initial_state(fsm, signal, data):
#     pass

class testfsm(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        initial_state = mock.Mock()
        self.fsm = fsm(current = initial_state)
        self.fsm.init(initial_state)
        initial_state.assert_called_once_with(self.fsm, SIGNAL_ENTRY, None)

    def test_transition(self):
        new_state_machine = fsm("running")

    def test_send_signal(self):
        new_state_machine = fsm("running")

if __name__ == '__main__':
    unittest.main()

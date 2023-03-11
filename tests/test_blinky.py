import unittest
from src.MyState import MyState, SIGNAL_ENTRY, SIGNAL_EXIT, SIGNAL_USER_START
from src.state_machine import fsm
from unittest import mock
from unittest.mock import patch

class testmystate(unittest.TestCase):
    def setUp(self):
        self.state = MyState()
        self.fsm = fsm(initial=self.state.on_entry)

    def test_on_entry(self):
        with mock.patch.object(self.state, 'on_entry') as mock_on_entry:
            self.fsm.transition(self.state.on_entry)
            mock_on_entry.assert_called_once_with(self.fsm, SIGNAL_ENTRY, None)

def test_on_exit(self):
        with mock.patch.object(self.state, 'on_exit') as mock_on_exit:
            self.fsm.transition(self.state.on_entry)
            self.fsm.transition(self.state.on_exit)
            mock_on_exit.assert_called_once_with(self.fsm, SIGNAL_EXIT, None)

def test_on_signal(self):
    with mock.patch.object(self.state, 'on_signal') as mock_on_signal:
        self.fsm.send_signal(SIGNAL_USER_START, "some data")
        mock_on_signal.assert_called_once_with(self.fsm, SIGNAL_USER_START, "some data")

if __name__ == '__main__':
    unittest.main()

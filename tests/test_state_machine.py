import unittest
from src.state_machine import fsm, SIGNAL_ENTRY, SIGNAL_EXIT, SIGNAL_USER_START
from unittest import mock

class testfsm(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        initial_state = mock.Mock(return_value=None)
        fsm_instance = fsm(initial_state)

        self.assertEqual(initial_state.call_count, 1)
        initial_state.assert_called_once_with(fsm_instance, SIGNAL_ENTRY, None)

if __name__ == '__main__':
    unittest.main()

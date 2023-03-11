import unittest
from src.state_machine import fsm, SIGNAL_ENTRY, SIGNAL_EXIT, SIGNAL_USER_START
from unittest import mock

class testfsm(unittest.TestCase):
    def setUp(self):
        pass

    def test_init_sends_entry_signal(self):
        initial_state = mock.Mock(return_value=None)
        fsm_instance = fsm(initial_state)

        self.assertEqual(initial_state.call_count, 1)
        initial_state.assert_called_once_with(fsm_instance, SIGNAL_ENTRY, None)

    # def test_transition_sends_exit_and_entry_signals(self):
    #     current_state_mock = mock.Mock()
    #     target_state_mock = mock.Mock(return_value=None)

    #     fsm_instance = fsm(current_state_mock)
    #     fsm_instance.transition(target_state_mock)

    #     current_state_mock.assert_has_calls(
    #         [
    #             mock.call(fsm_instance, SIGNAL_ENTRY, None),
    #             mock.call(fsm_instance, SIGNAL_EXIT, None)
    #         ]
    #     )

    #     target_state_mock.assert_has_calls(
    #         [
    #             mock.call(fsm_instance, SIGNAL_ENTRY, None)
    #         ]
    #     )

    def test_sends_signal_to_current_state(self):
        current_state_mock = mock.Mock()

        def on_signal(fsm, signal, data):
            if signal == SIGNAL_USER_START:
                print("woohoo", data)

        current_state_mock.on_signal = on_signal

        fsm_instance = fsm(current_state_mock)
        fsm_instance.send_signal(SIGNAL_USER_START, "some data")

        result = current_state_mock.on_signal(fsm_instance, SIGNAL_USER_START, "some data")

        current_state_mock.assert_has_calls(
            [
                mock.call(fsm_instance, SIGNAL_ENTRY, None),
                mock.call(fsm_instance, SIGNAL_USER_START, "some data")
            ]
        )


if __name__ == '__main__':
    unittest.main()

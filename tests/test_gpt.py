# import unittest
# from src.gpt import StateMachine

# class TestStateMachine(unittest.TestCase):
#     def setUp(self):
#         self.sm = StateMachine('off')
#         self.sm.add_transition('start', 'on')
#         self.sm.add_transition('process', 'processing')
#         self.sm.add_transition('finish', 'off')
#         self.sm.add_transition('error', 'error')

#     def test_initial_state(self):
#         self.assertEqual(self.sm.get_state(), 'off')

#     def test_start_transition(self):
#         self.sm.handle_event('start')
#         self.assertEqual(self.sm.get_state(), 'on')

#     def test_process_transition(self):
#         self.sm.handle_event('start')
#         self.sm.handle_event('process')
#         self.assertEqual(self.sm.get_state(), 'processing')

#     def test_finish_transition(self):
#         self.sm.handle_event('start')
#         self.sm.handle_event('process')
#         self.sm.handle_event('finish')
#         self.assertEqual(self.sm.get_state(), 'off')

#     def test_error_transition(self):
#         self.sm.handle_event('error')
#         self.assertEqual(self.sm.get_state(), 'error')

# if __name__ == '__main__':
#     unittest.main()

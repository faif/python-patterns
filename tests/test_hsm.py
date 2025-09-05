import unittest
from unittest.mock import patch

from patterns.other.hsm.hsm import (
    Active,
    HierachicalStateMachine,
    Standby,
    Suspect,
    UnsupportedMessageType,
    UnsupportedState,
    UnsupportedTransition,
)


class HsmMethodTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.hsm = HierachicalStateMachine()

    def test_initial_state_shall_be_standby(cls):
        cls.assertEqual(isinstance(cls.hsm._current_state, Standby), True)

    def test_unsupported_state_shall_raise_exception(cls):
        with cls.assertRaises(UnsupportedState):
            cls.hsm._next_state("missing")

    def test_unsupported_message_type_shall_raise_exception(cls):
        with cls.assertRaises(UnsupportedMessageType):
            cls.hsm.on_message("trigger")

    def test_calling_next_state_shall_change_current_state(cls):
        cls.hsm._current_state = Standby  # initial state
        cls.hsm._next_state("active")
        cls.assertEqual(isinstance(cls.hsm._current_state, Active), True)
        cls.hsm._current_state = Standby(cls.hsm)  # initial state

    def test_method_perform_switchover_shall_return_specifically(cls):
        """Exemplary HierachicalStateMachine method test.
        (here: _perform_switchover()). Add additional test cases..."""
        return_value = cls.hsm._perform_switchover()
        expected_return_value = "perform switchover"
        cls.assertEqual(return_value, expected_return_value)


class StandbyStateTest(unittest.TestCase):
    """Exemplary 2nd level state test class (here: Standby state). Add missing
    state test classes..."""

    @classmethod
    def setUpClass(cls):
        cls.hsm = HierachicalStateMachine()

    def setUp(cls):
        cls.hsm._current_state = Standby(cls.hsm)

    def test_given_standby_on_message_switchover_shall_set_active(cls):
        cls.hsm.on_message("switchover")
        cls.assertEqual(isinstance(cls.hsm._current_state, Active), True)

    def test_given_standby_on_message_switchover_shall_call_hsm_methods(cls):
        with (
            patch.object(cls.hsm, "_perform_switchover") as mock_perform_switchover,
            patch.object(cls.hsm, "_check_mate_status") as mock_check_mate_status,
            patch.object(
                cls.hsm, "_send_switchover_response"
            ) as mock_send_switchover_response,
            patch.object(cls.hsm, "_next_state") as mock_next_state,
        ):
            cls.hsm.on_message("switchover")
            cls.assertEqual(mock_perform_switchover.call_count, 1)
            cls.assertEqual(mock_check_mate_status.call_count, 1)
            cls.assertEqual(mock_send_switchover_response.call_count, 1)
            cls.assertEqual(mock_next_state.call_count, 1)

    def test_given_standby_on_message_fault_trigger_shall_set_suspect(cls):
        cls.hsm.on_message("fault trigger")
        cls.assertEqual(isinstance(cls.hsm._current_state, Suspect), True)

    def test_given_standby_on_message_diagnostics_failed_shall_raise_exception_and_keep_in_state(
        cls,
    ):
        with cls.assertRaises(UnsupportedTransition):
            cls.hsm.on_message("diagnostics failed")
        cls.assertEqual(isinstance(cls.hsm._current_state, Standby), True)

    def test_given_standby_on_message_diagnostics_passed_shall_raise_exception_and_keep_in_state(
        cls,
    ):
        with cls.assertRaises(UnsupportedTransition):
            cls.hsm.on_message("diagnostics passed")
        cls.assertEqual(isinstance(cls.hsm._current_state, Standby), True)

    def test_given_standby_on_message_operator_inservice_shall_raise_exception_and_keep_in_state(
        cls,
    ):
        with cls.assertRaises(UnsupportedTransition):
            cls.hsm.on_message("operator inservice")
        cls.assertEqual(isinstance(cls.hsm._current_state, Standby), True)

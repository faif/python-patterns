from unittest.mock import patch

import pytest

from patterns.other.hsm.hsm import (
    Active,
    HierachicalStateMachine,
    Standby,
    Suspect,
    UnsupportedMessageType,
    UnsupportedState,
    UnsupportedTransition,
)


class TestHsmMethod:
    @classmethod
    def setup_class(cls):
        cls.hsm = HierachicalStateMachine()

    def test_initial_state_shall_be_standby(cls):
        assert isinstance(cls.hsm._current_state, Standby)

    def test_unsupported_state_shall_raise_exception(cls):
        with pytest.raises(UnsupportedState):
            cls.hsm._next_state("missing")

    def test_unsupported_message_type_shall_raise_exception(cls):
        with pytest.raises(UnsupportedMessageType):
            cls.hsm.on_message("trigger")

    def test_calling_next_state_shall_change_current_state(cls):
        cls.hsm._current_state = Standby  # initial state
        cls.hsm._next_state("active")
        assert isinstance(cls.hsm._current_state, Active)
        cls.hsm._current_state = Standby(cls.hsm)  # initial state

    def test_method_perform_switchover_shall_return_specifically(cls):
        """Exemplary HierachicalStateMachine method test.
        (here: _perform_switchover()). Add additional test cases..."""
        return_value = cls.hsm._perform_switchover()
        expected_return_value = "perform switchover"
        assert return_value == expected_return_value


class TestStandbyState:
    """Exemplary 2nd level state test class (here: Standby state). Add missing
    state test classes..."""

    @classmethod
    def setup_class(cls):
        cls.hsm = HierachicalStateMachine()

    def setup_method(cls):
        cls.hsm._current_state = Standby(cls.hsm)

    def test_given_standby_on_message_switchover_shall_set_active(cls):
        cls.hsm.on_message("switchover")
        assert isinstance(cls.hsm._current_state, Active)

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
            assert mock_perform_switchover.call_count == 1
            assert mock_check_mate_status.call_count == 1
            assert mock_send_switchover_response.call_count == 1
            assert mock_next_state.call_count == 1

    def test_given_standby_on_message_fault_trigger_shall_set_suspect(cls):
        cls.hsm.on_message("fault trigger")
        assert isinstance(cls.hsm._current_state, Suspect)

    def test_given_standby_on_message_diagnostics_failed_shall_raise_exception_and_keep_in_state(
        cls,
    ):
        with pytest.raises(UnsupportedTransition):
            cls.hsm.on_message("diagnostics failed")
        assert isinstance(cls.hsm._current_state, Standby)

    def test_given_standby_on_message_diagnostics_passed_shall_raise_exception_and_keep_in_state(
        cls,
    ):
        with pytest.raises(UnsupportedTransition):
            cls.hsm.on_message("diagnostics passed")
        assert isinstance(cls.hsm._current_state, Standby)

    def test_given_standby_on_message_operator_inservice_shall_raise_exception_and_keep_in_state(
        cls,
    ):
        with pytest.raises(UnsupportedTransition):
            cls.hsm.on_message("operator inservice")
        assert isinstance(cls.hsm._current_state, Standby)

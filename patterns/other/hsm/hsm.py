"""
Implementation of the HSM (hierarchical state machine) or
NFSM (nested finite state machine) C++ example from
http://www.eventhelix.com/RealtimeMantra/HierarchicalStateMachine.htm#.VwqLVEL950w
in Python

- single source 'message type' for state transition changes
- message type considered, messages (comment) not considered to avoid complexity
"""


class UnsupportedMessageType(BaseException):
    pass


class UnsupportedState(BaseException):
    pass


class UnsupportedTransition(BaseException):
    pass


class HierachicalStateMachine:
    def __init__(self):
        self._active_state = Active(self)  # Unit.Inservice.Active()
        self._standby_state = Standby(self)  # Unit.Inservice.Standby()
        self._suspect_state = Suspect(self)  # Unit.OutOfService.Suspect()
        self._failed_state = Failed(self)  # Unit.OutOfService.Failed()
        self._current_state = self._standby_state
        self.states = {
            "active": self._active_state,
            "standby": self._standby_state,
            "suspect": self._suspect_state,
            "failed": self._failed_state,
        }
        self.message_types = {
            "fault trigger": self._current_state.on_fault_trigger,
            "switchover": self._current_state.on_switchover,
            "diagnostics passed": self._current_state.on_diagnostics_passed,
            "diagnostics failed": self._current_state.on_diagnostics_failed,
            "operator inservice": self._current_state.on_operator_inservice,
        }

    def _next_state(self, state):
        try:
            self._current_state = self.states[state]
        except KeyError:
            raise UnsupportedState

    def _send_diagnostics_request(self):
        return "send diagnostic request"

    def _raise_alarm(self):
        return "raise alarm"

    def _clear_alarm(self):
        return "clear alarm"

    def _perform_switchover(self):
        return "perform switchover"

    def _send_switchover_response(self):
        return "send switchover response"

    def _send_operator_inservice_response(self):
        return "send operator inservice response"

    def _send_diagnostics_failure_report(self):
        return "send diagnostics failure report"

    def _send_diagnostics_pass_report(self):
        return "send diagnostics pass report"

    def _abort_diagnostics(self):
        return "abort diagnostics"

    def _check_mate_status(self):
        return "check mate status"

    def on_message(self, message_type):  # message ignored
        if message_type in self.message_types.keys():
            self.message_types[message_type]()
        else:
            raise UnsupportedMessageType


class Unit:
    def __init__(self, HierachicalStateMachine):
        self.hsm = HierachicalStateMachine

    def on_switchover(self):
        raise UnsupportedTransition

    def on_fault_trigger(self):
        raise UnsupportedTransition

    def on_diagnostics_failed(self):
        raise UnsupportedTransition

    def on_diagnostics_passed(self):
        raise UnsupportedTransition

    def on_operator_inservice(self):
        raise UnsupportedTransition


class Inservice(Unit):
    def __init__(self, HierachicalStateMachine):
        self._hsm = HierachicalStateMachine

    def on_fault_trigger(self):
        self._hsm._next_state("suspect")
        self._hsm._send_diagnostics_request()
        self._hsm._raise_alarm()

    def on_switchover(self):
        self._hsm._perform_switchover()
        self._hsm._check_mate_status()
        self._hsm._send_switchover_response()


class Active(Inservice):
    def __init__(self, HierachicalStateMachine):
        self._hsm = HierachicalStateMachine

    def on_fault_trigger(self):
        super().perform_switchover()
        super().on_fault_trigger()

    def on_switchover(self):
        self._hsm.on_switchover()  # message ignored
        self._hsm.next_state("standby")


class Standby(Inservice):
    def __init__(self, HierachicalStateMachine):
        self._hsm = HierachicalStateMachine

    def on_switchover(self):
        super().on_switchover()  # message ignored
        self._hsm._next_state("active")


class OutOfService(Unit):
    def __init__(self, HierachicalStateMachine):
        self._hsm = HierachicalStateMachine

    def on_operator_inservice(self):
        self._hsm.on_switchover()  # message ignored
        self._hsm.send_operator_inservice_response()
        self._hsm.next_state("suspect")


class Suspect(OutOfService):
    def __init__(self, HierachicalStateMachine):
        self._hsm = HierachicalStateMachine

    def on_diagnostics_failed(self):
        super().send_diagnostics_failure_report()
        super().next_state("failed")

    def on_diagnostics_passed(self):
        super().send_diagnostics_pass_report()
        super().clear_alarm()  # loss of redundancy alarm
        super().next_state("standby")

    def on_operator_inservice(self):
        super().abort_diagnostics()
        super().on_operator_inservice()  # message ignored


class Failed(OutOfService):
    """No need to override any method."""

    def __init__(self, HierachicalStateMachine):
        self._hsm = HierachicalStateMachine

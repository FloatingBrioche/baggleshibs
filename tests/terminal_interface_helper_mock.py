from unittest.mock import Mock

class TerminalInterfaceHelperMock(object):
    def __init__(self):
        self._expected_calls = []
        self._provided_inputs = []
        self.console = Mock()

    def expect_print(self, message):
        self._expected_calls.append(message + "\n")

    def provide(self, input):
        self._provided_inputs.append(input)

    def write(self, message):
        expected_call = self._expected_calls.pop(0)
        if expected_call != message:
            raise AssertionError(
                f"Expected '{expected_call}', got '{message}'")

    def get_input(self):
        return self._provided_inputs.pop(0) + "\n"
    


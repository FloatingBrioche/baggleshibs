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
    

mock_io = Mock()

mock_io.get_input.side_effect = [
    "Egg Face", 
# ship, v/h, row, col
    1, 'h', 1, 1,   
    1, 'h', 2, 1,
    1, 'h', 3, 1,
    1, 'h', 4, 1,
    1, 'h', 5, 1,
    'ready',
    "Blob Face",
    1, 'h', 1, 1,   
    1, 'h', 2, 1,
    1, 'h', 3, 1,
    1, 'h', 4, 1,
    1, 'h', 5, 1,
    'ready',
    # game starts
    ## Destroy first ship
    1, 1,
    "ready",
    1, 1,
    "ready",
    1, 2,
    "ready",
    1, 2,
    "ready",

    ## Destroy second ship
    2, 1,
    "ready",
    2, 1,
    "ready",
    2, 2,
    "ready",
    2, 2,
    "ready",
    2, 3,
    "ready",
    2, 3,
    "ready",

    ## Destroy third ship
    3, 1,
    "ready",
    3, 1,
    "ready",
    3, 2,
    "ready",
    3, 2,
    "ready",
    3, 3,
    "ready",
    3, 3,
    "ready",

    ## Destroy fourth ship
    4, 1,
    "ready",
    4, 1,
    "ready",
    4, 2,
    "ready",
    4, 2,
    "ready",
    4, 3,
    "ready",
    4, 3,
    "ready",
    4, 4,
    "ready",
    4, 4,
    "ready",

    ## Destroy fifth ship
    5, 1,
    "ready",
    5, 1,
    "ready",
    5, 2, 
    "ready",
    5, 2,
    "ready",
    5, 3,
    "ready",
    5, 3,
    "ready",
    5, 4,
    "ready",
    5, 4,
    "ready",
    5, 5,
    "ready",
    5, 5,
    "ready"
    ]
    


from dataclasses import dataclass, field


@dataclass
class Ship:
    length: int
    health: int = field(init=False)
    body: list = field(init=False)

    def __post_init__(self):
        self.health = self.length
        self.body = ["S" for _ in range(self.length)]




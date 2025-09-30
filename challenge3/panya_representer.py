from human import Human

class PanyaRepresenter:
    def __init__(self, baby: Human, grown: Human ):
        self.baby = baby
        self.grown = grown

    def __str__(self) -> None:
        return (f"{self.baby}\n\nGrew up to become the \U0001F410\n\n{self.grown}")

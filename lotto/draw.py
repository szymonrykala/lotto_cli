from datetime import datetime
from dataclasses import asdict, dataclass


@dataclass
class LottoDraw():
    
    index:int
    date: datetime.date
    numbers: tuple[int]

    def __init__(self, draw_string: str) -> None:
        index, date_string, numbers_str = draw_string.strip().split()

        self.index: int = int(index[:-1])

        self.date: datetime.date = datetime.strptime(
            date_string,
            '%d.%m.%Y'
        ).date()

        self.numbers: tuple[int] = tuple(
            int(number)
            for number in numbers_str.split(',')
        )

    def as_dict(self):
        return asdict(self)
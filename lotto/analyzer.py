from draw import LottoDraw
from collections import Counter


class LottoResultsAnalyzer():
    __INF = 9999999

    def __init__(self, results: tuple[LottoDraw]) -> None:
        self.__results = results
        self.__numbers_occurence: list[tuple[str, int]] = \
            self.__count_occurence_of_numbers()

    @property
    def counted_numbers(self) -> dict[str, int]:
        return dict(self.__numbers_occurence)

    @property
    def draws_count(self) -> int:
        return len(self.__numbers_occurence)

    def load_draws_count(self, draws_count=__INF) -> None:
        '''
            Loads 'draws_count' on last draws to analyze
        '''
        self.__numbers_occurence = \
            self.__count_occurence_of_numbers(draws_count)

    def __count_occurence_of_numbers(self, draws_count=__INF):
        numbers = []
        for row in self.__results[-draws_count:]:
            numbers.extend(row.numbers)

        counted = Counter(numbers)
        return sorted(counted.items(), key=lambda x: -x[1])

    def get_less_common_numbers(self, count: int = 6) -> list[tuple[str, int]]:
        return self.__numbers_occurence[-count:]

    def get_most_common_numbers(self, count: int = 6) -> list[tuple[str, int]]:
        return self.__numbers_occurence[:count]

    def get_medium_common_numbers(self, count: int = 6) -> list[tuple[str, int]]:
        if count > 24:
            count = 24

        center = int(len(self.__numbers_occurence)/2)
        start = int(center - (count/2))
        end = int(center + (count/2))

        return self.__numbers_occurence[start:end]

    def get_draw(self, num: int = 0) -> LottoDraw:
        '''
            '0' is the most recent one;
            '1' is on befeore the last one etc
        '''
        return self.__results[len(self.__results)-num-1]

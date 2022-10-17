from datetime import datetime
from http import client
from os import path
from draw import LottoDraw


class LottoResultsManager():
    URL = {
        "host": "www.mbnet.com.pl",
        "path": "/dl.txt"
    }

    __FILE_PATH:str

    def __init__(self, file_path='./results.txt') -> None:
        self.__FILE_PATH = path.abspath(file_path)
        self.__lotto_results: tuple[LottoDraw] = ()

    @property
    def results(self):
        return self.__lotto_results

    def load_results(self) -> None:
        if self.__file_is_up_to_date():
            results = self.__get_results_from_file()
        else:
            results = self.__get_results_from_internet()

        self.__lotto_results = self.__parse_data(results)

    def __file_is_up_to_date(self, time_span: int = 24) -> bool:
        if path.exists(self.__FILE_PATH):
            modified = path.getmtime(self.__FILE_PATH)
            now = datetime.now().timestamp()

            return now > (modified + time_span * 3600)
        else:
            return False

    def __get_results_from_file(self) -> str:
        with open(self.__FILE_PATH, newline='\n', encoding='UTF8') as file:
            data = file.read()
            file.close()
            return data

    def __get_results_from_internet(self) -> str:
        conn = client.HTTPConnection(self.URL.get("host"), 80)
        conn.request("GET", self.URL.get("path"))
        resp = conn.getresponse()

        if resp.status != 200:
            raise client.HTTPException(
                "Error while getting lotto results from internet"
            )

        data = resp.read().decode()
        self.__save_to_file(data)
        return data

    def __save_to_file(self, data: str) -> None:
        with open(self.__FILE_PATH, 'w+', newline='', encoding='UTF8') as file:
            file.write(data.strip())
            file.close()

    def __parse_data(self, data: str) -> tuple[LottoDraw]:
        rows = []

        for row in data.split("\n"):
            row and rows.append(LottoDraw(row))
        return rows

from multiprocessing.dummy import Manager
from results_manager import LottoResultsManager
from analyzer import LottoResultsAnalyzer
import typer
import json



app = typer.Typer()



manager = LottoResultsManager('./data/results.txt')
manager.load_results()

analyzer = LottoResultsAnalyzer(manager.results)


@app.command()
def least_common_numbers(count:int=6):
    print(analyzer.get_less_common_numbers(count))


@app.command()
def most_common_numbers(count:int=6):
    print(analyzer.get_most_common_numbers(count))


@app.command()
def numbers_occurence():
    print(json.dumps(analyzer.counted_numbers,indent=4))



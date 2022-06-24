import pathlib
import csv

BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("../data/alunos.csv").resolve()


def load_csv():
    data = []
    list_school = {}
    with open(DATA_PATH, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')

        for row in csv_reader:
            row['ano'] = int(row['ano'])
            row['nota_semestre_1'] = float(row['nota_semestre_1'])
            row['nota_semestre_2'] = float(row['nota_semestre_2'])
            row['faltas'] = int(row['faltas'])
            row['nota_exame'] = float(row['nota_exame'])
            data.append(row)

            list_school[row['escola']] = 0
    return data, list_school


load_csv()
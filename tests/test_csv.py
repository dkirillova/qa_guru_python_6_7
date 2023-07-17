import csv
import os
from .conftest import resources_path


def test_create_csv_file():
    file_path = os.path.join(resources_path, 'eggs.csv')
    data = [['Anna', 'Pavel', 'Peter'], ['Alex', 'Serj', 'Yana']]

    with open(file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerows(data)

    assert os.path.exists(file_path)


def test_open_csv_file():
    file_path = os.path.join(resources_path, 'eggs.csv')

    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        rows = list(csvreader)

    for row in rows:
        print(row)

    assert len(row) == 3

    os.remove(file_path)


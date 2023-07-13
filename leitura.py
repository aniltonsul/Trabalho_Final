import csv

filename = "cep_cidade.csv"
separator = ";"

def read_csv_file():
    with open(filename, 'r', newline='', encoding='latin-1') as file:
        reader = csv.reader(file, delimiter=separator)
        header = next(reader)
        column_indices = [header.index("cidades"),header.index("cep")]
        extracted_columns = [[] for _ in range(len(column_indices))]
        data = []
        for row in reader:
            row_data = []
            for i, index in enumerate(column_indices):
                row_data.append(row[index])
            data.append(row_data)
        return data
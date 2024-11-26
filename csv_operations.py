import csv

CSV_FILE = "data.csv"

def read_csv():
    # Read the CSV file and return a list of rows
    table = []
    with open(CSV_FILE, mode="r") as file:
        reader = csv.reader(file)
        for line in reader:
            table.append(line)
    return table


def write_csv(table):
    # Write rows to the CSV file
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(table)

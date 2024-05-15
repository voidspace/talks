import csv
from new_stock.stock import Stock

# CSV reading

def read_stock_csv(filename):
    '''
    Read a CSV file into a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(Stock.from_row(row))
    return records

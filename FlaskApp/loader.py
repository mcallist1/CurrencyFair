import csv
import sqlite3

def main():
    conn = sqlite3.connect("db.sqlite")
    conn.execute('DROP TABLE history')
    conn.execute(
        'CREATE TABLE IF NOT EXISTS history (priceDate, currency, price)')

    cursor = conn.cursor();
    sql = ('INSERT INTO history VALUES(?, ?, ?)')
    with open('history.csv') as f:
        reader = csv.reader(f);
        next(reader, None)
        for line in reader:
            gbp = line[-2].strip()
            euro = line[13].strip()
            if gbp:
                 cursor.execute(sql, [line[0], 'GBP', line[-2]])
            if euro:
                 cursor.execute(sql, [line[0], 'EURO', line[13]])

    conn.commit()

main()
import csv

# чтение csv-файла
with open('file.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';',)
    # title = next(reader)
    for row in reader:
        print(row)

# чтение в словарь
with open('file.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    expensive = sorted(reader, key=lambda x: int(x['price']), reverse=True)

for record in expensive:
    print(record)


# запись в файл (для перезаписи режим 'w')
with open('file.csv', 'a', encoding="utf8", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    row = ['колбаса', 500, 'Микоян']
    writer.writerow(row)

# запись словаря в файл csv
data = [{
    'lastname': 'Иванов',
    'firstname': 'Пётр',
    'class_number': 9,
    'class_letter': 'А'
}, {
    'lastname': 'Кузнецов',
    'firstname': 'Алексей',
    'class_number': 9,
    'class_letter': 'В'
}, {
    'lastname': 'Меньшова',
    'firstname': 'Алиса',
    'class_number': 9,
    'class_letter': 'А'
}]

with open('dictwriter.csv', 'w', encoding="utf8", newline='') as f:
    writer = csv.DictWriter(
        f, fieldnames=list(data[0].keys()),
        delimiter=';')
    writer.writeheader()
    for d in data:
        writer.writerow(d)
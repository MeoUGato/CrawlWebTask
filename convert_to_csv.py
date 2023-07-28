import csv

with open('info.txt', 'r') as txt_file:
    lines = txt_file.readlines()

data = [line.strip().split(';') for line in lines]

with open('data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)

import csv
header=[]
file = open('qwerty.csv')
csvreader = csv.reader(file)
header = next(csvreader)
print(header)


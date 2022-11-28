import csv
with open('simple.csv') as f:
    csv_reader=csv.reader(f)
    headers=next(csv_reader)
    data=[]
    for line in csv_reader:
        data.append(line)

x_index=0
sum_of_division = 0
for x in data[0]:
    y_index = 0
    for y in data[1]:
        if x_index == 0 and y_index == 0:
            sum_of_division += (int(x) / int(y))
        elif x_index == 1 and y_index == 1:
            sum_of_division+=int(x)/int(y)
        elif x_index == 2 and y_index == 2:
            sum_of_division+=int(x)/int(y)
        y_index += 1
    x_index += 1
def calculate():
    return sum_of_division/len(headers)
print(round(calculate()))
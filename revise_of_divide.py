import csv
# CSV data first row=10,20,30
          #Second row=5,4,10
          # You have to program as 10/5+20/4+30/10=2+5+3=10/len(row)
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
        if x_index == y_index:
            sum_of_division += (int(x) / int(y))
        y_index += 1
    x_index += 1
def calculate():
    return sum_of_division/len(headers)
print('Average:',round(calculate()))
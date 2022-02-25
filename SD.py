import csv
import math
with open("data.csv", newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []

for i in range(len(file_data)):
    a = file_data[i][1]
    new_data.append(float(a))


# mean
def mean(new_data):
    n = len(new_data)
    sum = 0
    for i in new_data:
        sum += i
    mean = sum/n
    return mean

# squaring all the values


squared_list = []
for j in new_data:
    a = int(j)-mean(new_data)
    a = a ** 2
    squared_list.append(a)

# getting sum

sum = 0
for p in squared_list:
    sum += p


# dividing
result = sum / (len(new_data)-1)

# finding sqrt

sd = math.sqrt(result)
print(sd)

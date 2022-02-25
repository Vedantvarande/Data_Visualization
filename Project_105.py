import csv
from hashlib import new
import math
from unittest import result

with open('data_Pro105.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

# finding the mean


def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)

        mean = total/n
        return mean


squared_list = []
for number in data:
    a = int(number) - mean(data)
    a = a**2
    squared_list.append(a)

# getting sum
sum = 0
for i in squared_list:
    sum = sum + 1

result = sum/(len(data)-1)

std_deviation = math.sqrt(result)
print(std_deviation)

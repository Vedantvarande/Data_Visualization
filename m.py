import csv


with open("height-weight.csv", newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []

for i in range(len(file_data)):
    a = file_data[i][1]
    new_data.append(float(a))

n = len(new_data)
sum = 0
for j in new_data:
    sum = sum + j

mean = sum/n
print("Mean is: ", str(mean))

import csv
import pandas as pd
import plotly.express as px
with open("class2.csv", newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []

for i in range(len(file_data)):
    a = file_data[i][1]
    new_data.append(float(a))

sum = 0
n = len(new_data)

for j in new_data:
    sum += j

mean = sum/n
print("mean is: "+str(mean))

df = pd.read_csv("class2.csv")
fig = px.scatter(df, x="Student Number", y="Marks")
fig.update_layout(shapes=[
    dict(
        type='line',
        y0=mean, y1=mean,
        x0=0, x1=n
    )
])

fig.update_yaxes(rangemode="tozero")
fig.show()

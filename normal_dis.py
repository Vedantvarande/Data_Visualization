import plotly.express as px
import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
data_list = []
for i in range(0, 1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    a = dice1 + dice2
    data_list.append(a)


mean = sum(data_list) / len(data_list)
print("Mean of our dataset is: {}".format(mean))

median = statistics.median(data_list)
print("Median of our dataset is: {}".format(median))

mode = statistics.mode(data_list)
print("Mode of our dataset is: {}".format(mode))


std_deviation = statistics.stdev(data_list)
print("standard deviation of our dataset is {}".format(std_deviation))


first_std_deviation_start, first_std_deviation_end = mean - \
    std_deviation, mean + std_deviation
print("starting value of first deviation is: {}".format(first_std_deviation_start))
print("ending value of first deviation is: {}".format(first_std_deviation_end))

# finding values in 1 std dev
list_of_data_within_first_std_deviation = [
    result for result in data_list if result > first_std_deviation_start and result < first_std_deviation_end]

# finding the percent

first_std_dev_per = len(
    list_of_data_within_first_std_deviation)*100 / len(data_list)


print("{}% of data lies within first std deviation".format(first_std_dev_per))


# second level std dev

second_std_deviation_start, second_std_deviation_end = mean - \
    (2*std_deviation), mean + (2*std_deviation)
print("starting value of second deviation is: {}".format(
    second_std_deviation_start))
print("ending value of second deviation is: {}".format(second_std_deviation_end))

# finding values in 2 std dev
list_of_data_within_second_std_deviation = [
    result for result in data_list if result > second_std_deviation_start and result < second_std_deviation_end]

# finding the percent

second_std_dev_per = len(
    list_of_data_within_second_std_deviation)*100 / len(data_list)


print("{}% of data lies within second std deviation".format(second_std_dev_per))


# third level std dev

third_std_deviation_start, third_std_deviation_end = mean - \
    (3*std_deviation), mean + (3*std_deviation)
print("starting value of third deviation is: {}".format(
    third_std_deviation_start))
print("ending value of third deviation is: {}".format(third_std_deviation_end))

# finding values in 3 std dev
list_of_data_within_third_std_deviation = [
    result for result in data_list if result > third_std_deviation_start and result < third_std_deviation_end]

# finding the percent

third_std_dev_per = len(
    list_of_data_within_third_std_deviation)*100 / len(data_list)


print("{}% of data lies within third std deviation".format(third_std_dev_per))


# plotting the graph
fig = ff.create_distplot([data_list], ["DiceResult"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[
              0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(
    x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))

fig.add_trace(go.Scatter(
    x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))

fig.add_trace(go.Scatter(
    x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))

fig.add_trace(go.Scatter(
    x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))

fig.add_trace(go.Scatter(
    x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))


fig.add_trace(go.Scatter(
    x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.show()

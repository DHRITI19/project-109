import statistics
import random
import plotly.figure_factory as ff
import csv
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
mean = sum(score) / len(score)
median = statistics.median(score)
mode = statistics.mode(score)
std_deviation = statistics.stdev(score)
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviaiton_start, second_std_deviation_end = mean-(2*std_devation), mean+(2*std_devation)
third_std_devation_start, third_std_deviation_end = mean-(3*std_devation), mean+(3*std_devation)

thin_1_std_devation = [result for result in data if result > first_std_devation_start and result < first_std_deviation_end]
thin_2_std_devation = [result for result in data if result > second_std_devation_start and result < second_std_deviation_end]
thin_3_std_devation = [result for result in data if result > third_std_devation_start and result < third_std_deviation_end]
print("{}% of data lies within one standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice_result)))
print("Standard deviation of this data is {}".format(std_deviation))
print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))

fig = ff.create_distplot([dice_result], ["score"], show_hist = False)
fig.show()
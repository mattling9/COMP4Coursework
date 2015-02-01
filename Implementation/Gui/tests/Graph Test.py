import datetime
from matplotlib import pyplot as plt
from matplotlib.dates import date2num

data = [(datetime.datetime.strptime('01-02-2015', "%d-%m-%Y"), 123),
        (datetime.datetime.strptime('08-02-2015', "%d-%m-%Y"), 678),
        (datetime.datetime.strptime('15-02-2015', "%d-%m-%Y"), 987),
        (datetime.datetime.strptime('22-02-2015', "%d-%m-%Y"), 345)]

x = [date2num(date) for (date, value) in data]
y = [value for (date, value) in data]

fig = plt.figure()

graph = fig.add_subplot(111)

# Plot the data as a red line with round markers
graph.plot(x,y, 'r-o')

# Set the xtick locations to correspond to just the dates you entered.
graph.set_xticks(x)

# Set the xtick labels to correspond to just the dates you entered.
graph.set_xticklabels([date.strftime("%Y-%m-%d") for (date, value) in data])

plt.show()

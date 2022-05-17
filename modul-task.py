from matplotlib import pyplot as plt
from random import randint

profit_data = []

for i in range(12):
    sublist = []
    for i in range(31):
        sublist.append(randint(1000, 5000))
    profit_data.append(sublist)

def graph_profit_averages(data):
    profit_averages = []
    for set in data:
        profit_averages.append((sum(set)/len(set)))
    plt.plot(profit_averages)
    plt.show()


graph_profit_averages(profit_data)

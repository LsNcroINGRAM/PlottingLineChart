import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    #data = pd.read_csv(r'\Users\User\source\repos\LsNcroINGRAM\ReadForceSensor\Project1\data.csv')
    data = pd.read_csv(r'\Users\User\source\repos\LsNcroINGRAM\GeneratingData\GeneratingData\data.csv')
    x = data['x_value']
    y = data['y_value']

    plt.cla()

    plt.plot(x, y, label = 'Force')

    plt.legend(loc = 'upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval = 100)

plt.tight_layout()
plt.show()
from itertools import count
import matplotlib.pyplot as plt
import pandas as pd
from pandas.errors import EmptyDataError
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

def animate(i):
    try:
        #data = pd.read_csv(r'\Users\User\source\repos\LsNcroINGRAM\GeneratingData\GeneratingData\data.csv')
        data = pd.read_csv(r'\Users\User\source\repos\LsNcroINGRAM\ReadForceSensor\Project1\data.csv')
        x = data['x_value']
        y = data['y_value']

        plt.cla()

        plt.plot(x, y, label = 'Force')

        plt.legend(loc = 'upper left')
        plt.tight_layout()
    except EmptyDataError:
        df = pd.DataFrame()

ani = FuncAnimation(plt.gcf(), animate, interval = 5)

plt.tight_layout()
plt.show()
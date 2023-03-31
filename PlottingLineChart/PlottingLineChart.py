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
        #data = pd.read_csv(r'\Users\User\source\repos\LsNcroINGRAM\GeneratingData\GeneratingData\data.csv') #random value between 0 and 50
        data = pd.read_csv(r'\Users\User\source\repos\LsNcroINGRAM\ReadForceSensor\Project1\data.csv') #from force sensor
        x = data['x_value']
        y = data['y_value']
        plt.cla() #make sure the color of the plot is the same
        plt.plot(x, y, label = 'Force')
        plt.legend(loc = 'upper left')
        plt.ylim(-10, 50)

    except EmptyDataError:
        pass

ani = FuncAnimation(plt.gcf(), animate, interval = 5)

plt.tight_layout()
plt.show()
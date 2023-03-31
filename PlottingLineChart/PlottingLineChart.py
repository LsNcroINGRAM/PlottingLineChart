from itertools import count
import matplotlib.pyplot as plt
import pandas as pd
from pandas.errors import EmptyDataError
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')
MAX_FRAMES = 100

index = count()

def animate(i):
    try:
        data = pd.read_csv(r'\Users\User\source\repos\LsNcroINGRAM\ReadForceSensor\Project1\data.csv') #random value between 0 and 100
        #data = pd.read_csv(r'\Users\User\source\repos\LsNcroINGRAM\ReadForceSensor\Project1\data.csv') #from force sensor
        x = data['x_value']
        y = data['y_value']
        plt.cla() #make sure the color of the plot is the same
        plt.plot(x, y, label = 'Force (unit: N)')
        plt.legend(loc = 'upper left')
        plt.ylim(-1, 12)

    except EmptyDataError:
        pass

ani = FuncAnimation(plt.gcf(), animate, interval=10, save_count=MAX_FRAMES)


plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import numpy as np

t = mdates.drange(dt.datetime(2011, 10, 15), dt.datetime(2011, 11, 27),
                  dt.timedelta(hours=3))
y = np.sin(t)

fig, ax = plt.subplots()

ax.plot_date(t, y, 'b-')

ax.axvspan(*mdates.datestr2num(['10/27/2011', '11/2/2011']), color='red', alpha=0.5)

fig.autofmt_xdate()

plt.show()

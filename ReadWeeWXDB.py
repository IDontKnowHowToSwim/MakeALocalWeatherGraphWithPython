#!/usr/local/bin/python3

import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt

def fahrenheitToCelsis(degree_of_fahrenheit):
  if degree_of_fahrenheit is None:
    return None
  degree_of_celsis = (degree_of_fahrenheit - 32) / 9.0 * 5.0
  return degree_of_celsis

connect = sqlite3.connect('./weewx.sdb')
print("connect to sqlit")
c = connect.cursor()
extra_temp = ", ".join(["ExtraTemp" + str(x) for x in range(1, 6)])
extra_humid = ", ".join(["ExtraHumid" + str(x) for x in range(1, 6)])
sql_cmd = "SELECT DateTime, {}, {} FROM archive".format(extra_temp, extra_humid)
print ("{}\n\n".format(sql_cmd))

timestamps = []
temps = []
humids = []
#print(datetime.today())
for row in c.execute(sql_cmd):
  timestamp = row[0]
  temp = row[1:6]
  humid = row[6:]
  timestamps.append(datetime.fromtimestamp(timestamp))
  temps.append(fahrenheitToCelsis(temp[0]))
  humids.append(humid[0])
connect.close()

fig, ax = plt.subplots()
ax.plot(timestamps, temps, label="temperature")
ax.plot(timestamps, humids, label="humid")

plt.show()

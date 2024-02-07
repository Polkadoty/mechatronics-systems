# DOES NOT WORK (YET) File Read Error

import pandas as pd
import matplotlib.pyplot as plt


# Load in file
file0 = '.xlsx file path here'
T0 = pd.read_excel(file0)

# Samples
N = len(T0.iloc[:,1])
freq = 1000  # Hz
minute = 60  # minute in s
time = N / (minute * freq)
dt = (freq * minute) ** -1

# data
thermistordata = T0.iloc[:,1]
ICdata = T0.iloc[:,3]
thermocoupledata = T0.iloc[:,5]

# averages and SD
avgthermistor = thermistordata.mean()
uncthermistor = thermistordata.std()

avgIC = ICdata.mean()
uncIC = ICdata.std()

avgthermocouple = thermocoupledata.mean()
uncthermocouple = thermocoupledata.std()

# plots: thermistor, IC, thermocouple
plt.figure(figsize=(10, 8))
plt.title('Temperature Sensor Data @ Room Temperature')

plt.subplot(3, 1, 1)
plt.plot(range(0, int(time * freq), int(dt)), thermistordata, 'r--', linewidth=1.25)
plt.ylabel('Thermistor [Volt]')

plt.subplot(3, 1, 2)
plt.plot(range(0, int(time * freq), int(dt)), ICdata, 'k--', linewidth=1.25)
plt.ylabel('IC [Volt]')

plt.subplot(3, 1, 3)
plt.plot(range(0, int(time * freq), int(dt)), thermocoupledata, 'b--', linewidth=1.25)
plt.ylabel('Thermocouple [Celsius]')
plt.xlabel('Time [minutes]')

plt.tight_layout()
plt.show()

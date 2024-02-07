%% Room Temp
clear all; clc;

%Load in file 
file0 = ['lab2sheets\room-Temp','.xlsx'];
M0 = readmatrix(file0);

N = length(M0(:,2));

freq = 1000; %Hz
minute = 60; %minute in s
time = N/(minute*freq);
dt = (freq*minute)^-1;

%data
thermistordata = M0(:,2);
ICdata = M0(:,4);
thermocoupledata = M0(:,6);

%averages and SD
avgthermistor = mean(thermistordata);
uncthermistor = std(thermistordata);

avgIC = mean(ICdata);
uncIC = std(ICdata);

avgthermocouple = mean(thermocoupledata);
uncthermocouple = std(thermocoupledata);

%plots: thermistor, IC, thermocouple

subplot(3,1,1)
plot(0:dt:time-dt,thermistordata,'r--',"LineWidth",1.25)
title('Temperature Sensor Data @ Room Temperature')
ylabel('Thermistor [Volt]')


subplot(3,1,2)
plot(0:dt:time-dt,ICdata,'k--',"LineWidth",1.25)
ylabel('IC [Volt]')


subplot(3,1,3)
plot(0:dt:time-dt,thermocoupledata,'b--',"LineWidth",1.25)
ylabel('Thermocouple [Celsius]')

xlabel('Time [minutes]')


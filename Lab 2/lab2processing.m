%% Room Temp
clear all; clc;

%Load in file 
file0 = ['lab2sheets\room-Temp','.xlsx'];
M0 = readmatrix(file0);

%Sample
N = length(M0(:,2));
freq = 1000; %Hz
minute = 60; %minute in s
originaltime = N/(minute*freq);

i=0;

%find iteration of 1 minute
while i<N
    Q = length(M0(1:i,2));
    if Q/(minute*freq) == 1
        break;
    end
    i=i+1;
end

time1 = 1; % 1 minute of data
dt = (freq*minute)^-1;

%Resisitance
ohm = 1000; % 1k ohm resistor

%data
thermistordata = M0(1:i,2); % Thermistor convert to C ****
ICdata = 100.*(M0(1:i,4) - 0.5); %IC data converted to C
thermocoupledata = M0(1:i,6); 

%plots: thermistor, IC, thermocouple

figure(1);
plot(0:dt:time1-dt,thermistordata,'r-')
title('Temperature Sensor Data @ Room Temperature')
xlabel('Time [minutes]')
ylabel('Thermistor [Volts]')
grid on;

figure(2);
plot(0:dt:time1-dt,ICdata,'k-')
title('IC Temperature Sensor @ Room Temperature')
xlabel('Time [minutes]')
ylabel('IC [\circ Celsius]')
grid on;

figure(3);
plot(0:dt:time1-dt,thermocoupledata,'b-')
title('Thermocouple @ Room Temperature')
xlabel('Time [minutes]')
ylabel('Thermocouple [\circ Celsius]')
grid on;


% Confidence Interval in Laboratory
gamma = 0.95; %95 percent confidence

Fz = 0.5*(1+gamma);

nu = Q-1; %DOF

p = (1-gamma)/2; %probability

tstat = tinv(p,nu); %returns 

% (SAMPLE MEANS) Mean w/ Confidence Interval
avg_unc_thermistor = [mean(thermistordata) tstat*std(thermistordata)/sqrt(Q)];

avg_unc_IC = [mean(ICdata) tstat*std(ICdata)/sqrt(Q)];

avg_unc_thermocouple = [mean(thermocoupledata)  tstat*std(thermocoupledata)/sqrt(Q)];




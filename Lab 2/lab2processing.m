%% Room Temp
clear; clc;

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
thermistordata = M0(1:i,2)/0.05; % Thermistor convert to C 
ICdata = 100.*(M0(1:i,4) - 0.5); %IC data converted to C
thermocoupledata = M0(1:i,6); 

%plots: thermistor, IC, thermocouple

figure(1);
plot(0:dt:time1-dt,thermistordata,'r-')
title('Temperature Sensor Data @ Room Temperature','FontSize',15)
xlabel('Time [minutes]','FontSize',15)
ylabel('Thermistor [Volts]','FontSize',15)
grid on;

figure(2);
plot(0:dt:time1-dt,ICdata,'k-')
title('IC Temperature Sensor @ Room Temperature','FontSize',15)
xlabel('Time [minutes]','FontSize',15)
ylabel('IC [\circ Celsius]','FontSize',15)
grid on;

figure(3);
plot(0:dt:time1-dt,thermocoupledata,'b-')
title('Thermocouple @ Room Temperature','FontSize',15)
xlabel('Time [minutes]','FontSize',15)
ylabel('Thermocouple [\circ Celsius]','FontSize',15)
grid on;


% Confidence Interval in Laboratory
gamma = 0.95; %95 percent confidence

Fz = 0.5*(1+gamma);

nu = Q-1; %DOF

p = (1-gamma)/2; %probability

tstat = tinv(p,nu);  

% (SAMPLE MEANS) Mean w/ Confidence Interval

sd_thermistor = std(thermistordata);
sd_IC = std(ICdata);
sd_thermocouple = std(thermocoupledata);

<<<<<<< HEAD
function tau = calculateTimeConstant(V, t)
    % V(t) = c1 * (1 - exp(-t/tau))
    % Solve for tau
    % tau = -t / log(1 - V(t) / c1)
    
    c1 = max(V);
    % Assuming c1 is the maximum voltage value
    tau = -t / log(1 - V(end) / c1);
end

=======
avg_unc_thermistor = [mean(thermistordata) tstat*sd_thermistor/sqrt(Q)];
>>>>>>> d5b72aa8cd0a2339671db8f5b9be133c2f876dd6

avg_unc_IC = [mean(ICdata) tstat*sd_IC/sqrt(Q)];

avg_unc_thermocouple = [mean(thermocoupledata)  tstat*sd_thermocouple/sqrt(Q)];

% Get a list of all files and folders in the directory
Files = dir('Lab Files/*.xlsx');
i=1;
% Get a logical vector that tells which is a file
isFile = ~[Files.isdir];
figure()
% Loop only over the files
for iExcelSubject = 1:length(Files)
    if isFile(iExcelSubject)
        % Full path to file
        Report = fullfile('Lab Files', Files(iExcelSubject).name);
        % Read the table from the Excel file
        T = readtable(Report);
        % Do something with table T
        % ...
        time=0.001:0.001:10;
data=[T(:,2) T(:,4) T(:,6)];
data=table2array(data);
averages=mean(data,1);
[N,M]=size(T);
% 1:mems (x)
% 2:mems (y)
% 3:piezo (y)
CaliPiezo=10; %mV/g
CaliPiezo=CaliPiezo*1/1000/9.81; %V/(m/s^2)
data_norm=bsxfun(@minus, data , averages);
data_norm(:,3)=data_norm(:,3)/CaliPiezo/2.815;


V0=fft(data_norm(:,3));
Frequency=linspace(0,1000,N);
Amplitude1=2/N*real(abs(V0));
hold on;
figure(1)
plot(Frequency(1:N/2),Amplitude1(1:N/2))
title('Piezo (5 seconds)')
legend()

loc1=Amplitude1==max(Amplitude1(1:N/2));
NaturalFreqV0=Frequency(loc1);
NaturalFreqV0_5(i)=NaturalFreqV0(1);

i=i+1;
% N2=N/2;
% Frequency=linspace(0,1000,N2);
% data_norm(1:N2,:)=[];
% V0=fft(data_norm(:,1));
% Amplitude1=2/N2*real(abs(V0));
% hold on;
% figure(2)
% plot(Frequency(1:N2/2),Amplitude2(1:N2/2))
% title('Piezo (Last second)')
% legend()
    end
end
hold off;


figure();
hold on;
% Loop only over the files
for iExcelSubject = 1:length(Files)
    if isFile(iExcelSubject)
        % Full path to file
        Report = fullfile('Lab Files', Files(iExcelSubject).name);
        % Read the table from the Excel file
        T = readtable(Report);
        % Do something with table T
        % ...
        time=0.001:0.001:10;
data=[T(:,2) T(:,4) T(:,6)];
data=table2array(data);
averages=mean(data,1);
[N,M]=size(T);
% 1:mems (x)
% 2:mems (y)
% 3:piezo (y)
CaliPiezo=10; %mV/g
CaliPiezo=CaliPiezo*1/1000/9.81; %V/(m/s^2)
data_norm=bsxfun(@minus, data , averages);
data_norm(:,3)=data_norm(:,3)/CaliPiezo/2.815;


% V0=fft(data_norm(:,3));
% Frequency=linspace(0,1000,N);
% Amplitude1=2/N*real(abs(V0));
% hold on;
% figure(1)
% plot(Frequency(1:N/2),Amplitude1(1:N/2))
% title('Piezo (5 seconds)')
% legend()

N2=N/2;
Frequency=linspace(0,1000,N2);
data_norm(1:N2,:)=[];
V0=fft(data_norm(:,3));
Amplitude1=2/N2*real(abs(V0));
hold on;
figure(2)
plot(Frequency(1:N2/2),Amplitude1(1:N2/2))
title('Piezo (Last second)')
legend()

loc1=Amplitude1==max(Amplitude1(1:N2/2));
NaturalFreqV0=Frequency(loc1);
NaturalFreq_LastSec(i)=NaturalFreqV0(1);

i=i+1;
    end
end
hold off;

NaturalFreqV0_5
NaturalFreq_LastSec;
NaturalFreq_LastSec=NaturalFreq_LastSec(11:end)
Avg5SecFreq=mean(NaturalFreqV0_5)
AvgLastSecFreq=mean(NaturalFreq_LastSec)

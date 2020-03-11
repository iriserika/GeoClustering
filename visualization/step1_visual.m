clc
clear 
close all

fid = fopen('devicestatus_etl');
C = textscan(fid, '%f %f %s %s %s %s', 'Delimiter', ',');
fclose(fid);

latitude = C{1};
longitude = C{2};

plot(longitude, latitude, 'x');
xlabel('Longitude');
ylabel('Latitude');
grid on;
title('Visualization of Device Status Data');